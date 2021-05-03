import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/search_template")
def search_template():
    return render_template("search.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    if query:
        books = list(mongo.db.books.find({"$text": {"$search": query}}))
        ratings = list(mongo.db.reviews.aggregate(
            [{'$group': {'_id': '$book_id', 'average': {'$avg': '$rating'}}}]))
        for book in books:
            id = ObjectId(book["_id"])
            cover = mongo.db.covers.find_one(
                {"book_id": id})
            if cover is not None:
                book["cover"] = cover["cover"]

        return render_template(
            "display_searched_books.html", books=books, query=query, ratings=ratings)
    else:
        return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if (request.form.get("password") == request.form.get("password1")):
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/display_books/<age_group>")
def display_books(age_group):
    books = list(mongo.db.books.find({"age": age_group}))
    ratings = list(mongo.db.reviews.aggregate(
        [{'$group': {'_id': '$book_id', 'average': {'$avg': '$rating'}}}]))

    for book in books:
        id = ObjectId(book["_id"])
        cover = mongo.db.covers.find_one(
            {"book_id": id})
        if cover is not None:
            book["cover"] = cover["cover"]

    return render_template(
        "display_books.html", books=books, age_group=age_group, ratings=ratings)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        if session["user"] == username:
            revs = mongo.db.reviews.find({"created_by": username})
            users_revs = []
            # this part was borrowed from StackOverflow (see Readme.md)
            book_ids = []
            for rev in revs:
                book_ids.append((rev['_id'], rev['book_id']))

            for id, item in book_ids:
                book = mongo.db.books.find_one(
                    {"_id": item}, {"title": 1, "author": 1})
                review = mongo.db.reviews.find_one(
                    {"_id": id}, {"review_id": 1, "review": 1, "rating": 1})
                merged = {**book, **review}
                users_revs.append(merged)

            return render_template(
                "profile.html", users_revs=users_revs)
        return redirect(url_for("home"))

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review/", methods=["GET", "POST"])
def add_review():
    if "user" in session:
        if request.method == "POST":
            existing_book = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()})

            # if there's no such book in the db yet, it'll be added:
            if not existing_book:
                book = {
                    "title": request.form.get("title").lower(),
                    "author": request.form.get("author"),
                    "isbn": request.form.get("isbn"),
                    "category": request.form.getlist("category_name"),
                    "age": request.form.getlist("age_group"),
                }
                mongo.db.books.insert_one(book)

            book_id = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()})["_id"]

            # create document for reviews collection
            review = {
                "review": request.form.get("review"),
                "rating": int(request.form.get("rating")),
                "book_id": book_id,
                "created_by": session["user"]
            }
            mongo.db.reviews.insert_one(review)

            # create document for covers collection
            if not request.form.get("cover").endswith(('jpeg', 'png')):
                flash("Please enter a valid url!")
                result = {
                    "title": request.form.get("title").lower(),
                    "author": request.form.get("author"),
                    "isbn": request.form.get("isbn"),
                    "category": request.form.getlist("category_name"),
                    "age": request.form.getlist("age_group"),
                    "review": request.form.get("review"),
                    "rating": int(request.form.get("rating"))
                }
                return render_template("add_review.html", result=result)

            cover = {
                    "cover": request.form.get("cover"),
                    "book_id": book_id
                }
            mongo.db.covers.insert_one(cover)

            flash("Your Review Was Successfully Added")
            return render_template("home.html")

        book = mongo.db.books.find_one(
                {"title": request.form.get("title")})
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        ages = list(mongo.db.age_groups.find().sort("age_group", 1))
        result = {}
        return render_template(
            "add_review.html", book=book, categories=categories, ages=ages, result=result)
    return render_template("unauthorised_error.html")


@app.route("/add_review/<age_group>", methods=["GET", "POST"])
def add_review_by_age(age_group):
    if "user" in session:
        if request.method == "POST":
            existing_book = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()})

            # if there's no such book in the db yet, it'll be added:
            if not existing_book:
                book = {
                    "title": request.form.get("title").lower(),
                    "author": request.form.get("author"),
                    "isbn": request.form.get("isbn"),
                    "category": request.form.getlist("category_name"),
                    "age": request.form.getlist("age_group")
                }
                mongo.db.books.insert_one(book)

            book_id = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()})["_id"]

            # create document for reviews collection
            review = {
                "review": request.form.get("review"),
                "rating": int(request.form.get("rating")),
                "book_id": book_id,
                "created_by": session["user"]
            }
            mongo.db.reviews.insert_one(review)

            # create document for covers collection
            cover = mongo.db.covers.find_one(
                {"book_id": ObjectId(book_id)})
            if not cover:
                updated_cover = {
                    "cover": request.form.get("cover"),
                    "book_id": book_id
                }
                mongo.db.covers.insert_one(
                        {"book_id": ObjectId(book["_id"])}, updated_cover)

            flash("Your Review Was Successfully Added")
            return render_template("home")

        book = mongo.db.books.find_one(
                {"title": request.form.get("title")})
        categories = list(mongo.db.categories.find().sort("category_name", 1))
        ages = list(mongo.db.age_groups.find().sort("age_group", 1))
        result = {}
        return render_template(
            "add_review.html", book=book, categories=categories, ages=ages, age_group=age_group, result=result)

    return render_template("unauthorised_error.html")


@app.route("/add_review_by_title/<book_id>", methods=["GET", "POST"])
def add_review_by_title(book_id):
    if "user" in session:
        book = mongo.db.books.find_one(
                {"_id": ObjectId(book_id)})

        if request.method == "POST":
            updated_book = {
                "title": book["title"],
                "author": request.form.get("author"),
                "isbn": request.form.get("isbn"),
                "category": request.form.getlist("category_name"),
                "age": request.form.getlist("age_group")
            }
            mongo.db.books.update(
                {"_id": ObjectId(book["_id"])}, updated_book)

            # create document for reviews collection
            review = {
                "review": request.form.get("review"),
                "rating": int(request.form.get("rating")),
                "book_id": book["_id"],
                "created_by": session["user"]
            }
            mongo.db.reviews.insert_one(review)

            # create document for covers collection
            cover = mongo.db.covers.find_one(
                {"book_id": ObjectId(book_id)})
            if not cover:
                if request.form.get("cover"):
                    updated_cover = {
                        "cover": request.form.get("cover"),
                        "book_id": book_id
                    }
                    mongo.db.covers.insert_one(
                            {"book_id": ObjectId(book_id)}, updated_cover)

            flash("Your Review Was Successfully Added")

        categories = list(mongo.db.categories.find().sort("category_name", 1))
        ages = list(mongo.db.age_groups.find().sort("age_group", 1))
        return render_template(
            "add_review_by_title.html", book=book, categories=categories, ages=ages)
    return render_template("unauthorised_error.html")


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if "user" in session:
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        if session["user"] == review['created_by']:
            book = mongo.db.books.find_one(
                {"_id": ObjectId(review["book_id"])})
            cover = mongo.db.covers.find_one(
                {"book_id": ObjectId(review["book_id"])})

            if request.method == "POST":
                updated_book = {
                    "title": book["title"],
                    "author": request.form.get("author"),
                    "isbn": request.form.get("isbn"),
                    "category": request.form.getlist("category_name"),
                    "age": request.form.getlist("age_group")
                }
                mongo.db.books.update(
                    {"_id": ObjectId(book["_id"])}, updated_book)

                updated_review = {
                    "review": request.form.get("review"),
                    "rating": int(request.form.get("rating")),
                    "book_id": book["_id"],
                    "created_by": session["user"]
                }
                mongo.db.reviews.update(
                    {"_id": ObjectId(review_id)}, updated_review)

                if not cover:
                    updated_cover = {
                        "cover": request.form.get("cover"),
                        "book_id": book["_id"]
                    }
                    mongo.db.covers.insert_one(
                        {"book_id": ObjectId(book["_id"])}, updated_cover)

                flash("Your Review Was Successfully Updated")
                return redirect(url_for("profile", username=session["user"]))

            categories = list(
                mongo.db.categories.find().sort("category_name", 1))
            ages = list(mongo.db.age_groups.find().sort("age_group", 1))
            return render_template(
                "edit_review.html", review=review, book=book, categories=categories, ages=ages)

        return redirect(url_for("home"))
    return render_template("unauthorised_error.html")


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    if "user" in session:
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("Review Was Successfully Deleted")
        return render_template("home.html")

    return render_template("unauthorised_error.html")


@app.route("/get_categories")
def get_categories():
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if username == "admin":
            categories = list(
                mongo.db.categories.find().sort("category_name", 1))
            return render_template("categories.html", categories=categories)

    return render_template("unauthorised_error.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if username == "admin":
            if request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.insert_one(category)
                flash("New Category Added")
                return redirect(url_for("get_categories"))

            return render_template("add_category.html")

    return render_template("unauthorised_error.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if username == "admin":
            if request.method == "POST":
                submit = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.update(
                    {"_id": ObjectId(category_id)}, submit)
                flash("Category Successfully Updated")
                return redirect(url_for("get_categories"))

            category = mongo.db.categories.find_one(
                {"_id": ObjectId(category_id)})
            return render_template("edit_category.html", category=category)
    return render_template("unauthorised_error.html")


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if "user" in session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if username == "admin":
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category Successfully Deleted")
            return redirect(url_for("get_categories"))
    return render_template("unauthorised_error.html")


@app.route("/book_reviews/<book_id>")
def book_reviews(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    cover = mongo.db.covers.find_one({"book_id": ObjectId(book_id)})
    if cover is not None:
        book["cover"] = cover["cover"]
    reviews = mongo.db.reviews.find({"book_id": ObjectId(book_id)})
    ratings = list(mongo.db.reviews.aggregate(
        [{'$group': {'_id': '$book_id', 'average': {'$avg': '$rating'}}}]))

    return render_template(
        "book_reviews.html", book=book, reviews=reviews, ratings=ratings)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
