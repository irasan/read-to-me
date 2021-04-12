import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
from itertools import chain


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


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
                flash("Welcome, {}".format(
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


@app.route("/get_books1")
def get_books1():
    books = mongo.db.books1.find()
    return render_template("books1.html", books1=books)


@app.route("/get_books2")
def get_books2():
    books = mongo.db.books2.find()
    return render_template("books2.html", books2=books)


@app.route("/get_books3")
def get_books3():
    books = mongo.db.books3.find()
    return render_template("books3.html", books3=books)


@app.route("/get_books4")
def get_books4():
    books = mongo.db.books4.find()
    return render_template("books4.html", books4=books)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        revs = mongo.db.reviews.find({"created_by": username})
        users_revs = []
        # this part was borrowed from StackOverflow (see Readme.md)
        book_ids = []
        for rev in revs:
            book_ids.append((rev['_id'], rev['book_id']))
        print(book_ids)

        for id, item in book_ids:
            book = mongo.db.books.find_one(
                {"_id": item}, {"title": 1, "author": 1})
            print(book)
            review = mongo.db.reviews.find_one(
                {"_id": id}, {"review_id": 1, "review": 1, "rating": 1})
            print(review)
            merged = {**book, **review}
            print("Merged", merged)
            users_revs.append(merged)

        return render_template(
            "profile.html", users_revs=users_revs)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        existing_book = mongo.db.books.find_one(
            {"title": request.form.get("title").lower()})

        if not existing_book:
            book = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "isbn": request.form.get("isbn"),
                "category": request.form.get("category_name"),
                "age": request.form.get("age_group")
            }
            mongo.db.books.insert_one(book)

        book_id = mongo.db.books.find_one(
            {"title": request.form.get("title")})["_id"]

        review = {
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "book_id": book_id,
            "created_by": session["user"]
        }

        mongo.db.reviews.insert_one(review)
        flash("Your Review Successfully Added")
        return render_template("profile.html", username=session["user"])

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    ages = list(mongo.db.age_groups.find().sort("age_group", 1))
    return render_template(
        "add_review.html", categories=categories, ages=ages)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    book = mongo.db.books.find_one({"_id": ObjectId(review["book_id"])})

    if request.method == "POST":
        updated_book = {
            "title": book["title"],
            "author": request.form.get("author"),
            "isbn": request.form.get("isbn"),
            "category": request.form.get("category_name"),
            "age": request.form.get("age_group")
        }
        mongo.db.books.update(
            {"_id": ObjectId(book["_id"])}, updated_book)

        updated_review = {
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "book_id": book["_id"],
            "created_by": session["user"],
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, updated_review)
        flash("Your Review Was Successfully Edited")

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    ages = list(mongo.db.age_groups.find().sort("age_group", 1))
    return render_template(
        "edit_review.html", review=review, book=book, categories=categories, ages=ages)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
