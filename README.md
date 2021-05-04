# Read to me
![responsive website](https://github.com/irasan/read-to-me/blob/master/static/images/read-me-responsive.png)

This is a web service that allows its users to find the best childrens books, based on reviews and ratings of other users. 
There are thousands of books out there and while many of them might seem appealing or beautifully illustrated to adults, they are not 
necessarily insteresting for children. That's why this service will gather feedback on books from the point of view of a child. 
Also people tend to buy books that are well marketed and popular, leaving a small chance for short run or other great books to be found.
With the help of users, we aim to create a nice collection of children's books that are not always on the top shelves in bookstores.

This was the third of four Milestone Projects required to pass the Full Stack Web Development Program at Code Institute. The main 
requirements were to build a full-stack site using HTML, CSS, JavaScript, Python, Flask and MongoDB that allows users to manage a 
common dataset about a particular domain.

Click [here](http://irasan-read-to-me.herokuapp.com) to view the live website.


## UX

### Project goals
The primary goal of the project is to present a collection of favourite children’s books and help users to make easier decisions when 
purchasing new books. 

### Customers' goals
The main audience for this website consists of yound parents and grandparents who would like to promote reading in their homes.
Their main goal would be to find great books for children to read, to share their experiences regarding books they've read, as well as
save money and help other people to do so by preventing from investing in beautiful but not so interesting books.

Customers goals are:
* find best books for a certain age group;
* find books according to children’s interests;
* share feedback on books from the point of view of their children;
* see a list of their reviews and ratings;
* be able to update their reviews and ratings;
* be able to create a list of books to read and update it.

This website helps the users to meet their needs because: 
* the goals stated above were taken into consideration during all stages of the development process;
* users can register their profiles, create reviews on books and rate them;
* registered users can see a list of their reviews and ratings;
* registered users can create books-to-read lists;
* navigation is traditional and intuitive, the website in general is user friendly and accessible.

### Developer's Goals
This is a learning project and the main purpose of it's creating is to learn Python and how to connect a database to
the project. Another very improtant goal is to build a project that will be added to the portfolio. 

### Business Goals
This website may be used for indirect sales of books. In particular, links to bookstores may be added under the books, promoting
visitors to follow them and make purchases.

### User Stories
As a young parent/grandparent, I want:
* to cultivate love to books and promote reading for my kids, that's why I need to find the best books;
* to buy books that are loved by modern children and are not simply a tribute to traditions or well marketed;
* to create a list of nice books and update it when I bought something from it or am no longer interested;
* to share my thoughts about books that were read to my children and help other parents to make a decision.

As a reading child I want:
* to make use of a service like [goodreads.com](https://www.goodreads.com/) only specifically aimed for children;
* to share my feedback on books and read feedback of other children;
* to create lists of books that I want to read in the future.

### Wireframes
After thorough consideration of users' and developer's goals, the following 
[wireframes](https://github.com/irasan/read-to-me/blob/master/assets/wireframes/wireframes.pdf) were created. 

### Design Choices
The overall feel of the website is family friendly, simple, and fun. The following design choices were made in order to implement the game: 

#### Fonts
Josefin Slab was chosen as main font for the website. It features round, a bit Gothic letters and reminds fonts in children's books.
Logo and headings in footer were written with Gloria Hallelujah. This is fun, comic-like font based on handwriting and very easy to read. 
Both fonts were downloaded from [Google Fonts.](https://fonts.google.com/)

#### Icons
All icons were chosen for their obvious meaning so that they can be easily understood by everyone. Social media icons and icons on forms
(login, registration, adding and updating reviews) were implemented using [Font Awesome.](https://fontawesome.com/)
Links to social media in the Footer do not exist yet, so currently the icons lead to the main pages for each social media network.
Smiley faces for different ratings were downloaded from [here.](https://www.flaticon.com/packs/classics-2?word=emoji)

#### Colors
Color palette for this project was created using [Coolors.co](https://coolors.co) service.
It is recommended to choose bold and bright colors for children. Keeping in mind gender neutrality, the following were picked
for the project:
![color pallette](https://github.com/irasan/read-to-me/blob/master/assets/readme-images/colors.png)
During implementation of the project, in order to simplify it, all colors except the main background color were picked from those
available on [Materialize.](https://materializecss.com/color.html), but closely matching the palette.

 Design of the website in general is cheerful, bright, and playful in order to highlight it's purpose and audience.

#### Styling
For styling of the website Materialize framework was utilised:
* collapsible was used for display of user's reviews. It features book's title, author's name, rating, and two buttons for deleting and
updating in the header, and the review itself in the body, which is hidden until clicked on the header.
* navbar is responsive and collapses to a button on smaller screens. It also displays different tabs according to the type of user.
* footer features a short about section, popular links to pages on the website, and social media icons.
* categories are displayed using cards, making them all looking the same with category name and buttons for delete and edit.
* forms for login, registration, adding and editing reviews were nicely styled using available features.


## Features
This website features a few pages which visibility depends on the type of user. In particular, visitors of the site who 
haven't registered or logged in, will be able to see Home page with books divided by different age categories, lists of books in every age group,
and each individual book together with it's reviews. They will also be able to login or register.
Registered and logged in users will see two additional tabs: My reviews, featuring all the reviews they made, and Add Review.
Admin user, apart from the functionality mentioned above, will be able to manage book categories: add new, update, and delete them.

Many pages feature a sticky floating call-to-action buttons that allow to add reviews. The purpose of these buttons is highlighted in tooltips,
that appear when users hover over them.

Every page has a navbar and a footer for easier navigation throughout the site.

All pages are connected with each other, passing parameters and creating better UX. Particularly, if users click on the add review 
button from the home page (choosing an age group) or book page (in order to leave review on this particular book), the form template
will be pre-filled automatically with the key values (age, book title or book author).

### Home page
![home page](https://github.com/irasan/read-to-me/blob/master/static/images/read-me-responsive.png)

Home page displays 4 cards for books in different age groups. These are:
1. 0-2 years old: here users will find books with no or very little text as well as first nursery rhymes;
1. 3-5 years old: beautifully illustrated books with short stories and poems. Cartoon characters and first interests can also 
be found here;
1. 6-8 years old: books for children that start reading themselves as well as books with long stories where accent is on the
text, not the illustrations;
1. 9-12 years old: this category will contain adventure books and other fascinating stories that promote reading.

By clickign on any of the age group, a user will be redirected to the next page displaying all books in that particular category.

### Display of books
![books display page](https://github.com/irasan/read-to-me/blob/master/static/images/display-books.png)

This page features all books in a certain age group. Every book has a cover picture, it's title, author, categories, and average
rating. This average rating is based on all reviews that were left on each particular book. Titles are clickable and will direct user
to the book reviews page.

### Book reviews page
![book reviews page](https://github.com/irasan/read-to-me/blob/master/static/images/book-reviews.png)
This page displays a book with all it's reviews. It can be accessed from books display page or search results. 
At the top users will find book's cover, it's title, author's name, ISBN, age, categories, and average rating. 
Underneath there's a list of reviews left by users. There's a mention of the user who left that reviews and besides there's an emoji
that references user's opinion. There are 5 types of emojis - from sad and dispappointed to very happy one. 
This page also has a floating button that allows users to leave a review on the book featured there. When the form is loaded,
it will have book's title and author's name pre-filled for better user experience. However, the user needs to be registered or logged
in in order to access that page. 

### Create Account Page
This page features a simple form, where the user can input username and password twice. This form checks if the passwords match 
each other and if a user with. the same username already exists. If everything's fine a new user is created.
The form was kept deliberately simple to make better user experiences.

### Login page
This page features a very simple form for entering username and password. It has validation for length or incorrect username/
password with appropriate pop-up messages. If user entered everything correctly, Profile page will appear.

### Profile page
Users can find all their reviews under the Profile tab in navbar. It features a collapsible - a list of books that can be expanded
to show the review itself. It also features two buttons for delete and edit of the reviews.

### Add and edit review
Add review page is only accessible to registered users from Home page, Book reviews page or from the navbar. Depending on the way users access
this page, it might have pre-filled parts in the form. 
Edit review page is accessed from Profile page and also has pre-filled input fields. 
This was achieved by passing relevant parameters from the function and using value="{{ book.title }}" in the form. 

Validation of the <input> fields is handled in variety of ways:
* input type attributes are set to text, email, url and number where appropriate;
* minimum and maximum lengths limits are placed on the text input fields;
* dropdown menus are provided for rating, age group, and categories, so that those inputs will match documents in the database;
* the only field that is not required is text review, all others are mandatory. Cover image is required for new books and optional for 
books that already exist;
* additional validation was created for cover image urls. It was added to the function in app.py in order to check if the url 
ends with .jpeg or .png

### Manage categories
This page is only visible to admin user. It allows to add, edit and update book categories.

### Search
Search page is only displayed on small screens, as input field for search on medium and larger screens is located in navbar.
Search results will be displayed in the similar manner as books in age groups, featuring book covers, titles, author's names,
category, age group, and average rating.

### Error pages
There are two types of error pages: 404 error and unauthorised access error. 
Custom 404 error page states "Page Not Found" and features a button to return to Home page.
Unauthorised access page says "Only registered users here! To add, edit or delete reviews, please login or register" 
and displays to buttons for login or creating an account. This page will be displayed every time when a user tries 
to access a page that requires registration.

### Features Overview
#### Existing Features
* User registration and login - supported by MongoDB;
* Functionality to add new books and reviews on them;
* Possibility to update and delete reviews;
* Pre-filled forms for better user experience;
* Books can be distinquished by different age groups and categories;
* Books have covers stored in a separate collection;
* Calculation of book's average rating based on all the reviews that were left on this book;
* Emojis, that change according to the book rating from sad to very happy, on Book reviews page;
* Call for action buttons - help users to save time by adding reviews with pre-filled values;
* Search of books based on title, author name or category;
* Functionality to add, update, and delete book categories for admin user;
* Checks for direct input access for all pages that require users to be logged in.

### Features Left To implement
* Possibility to sort books according to their ratings or categories;
* Partial text book search;
* Preventing misspellings in book titles or authors' names;
* Granting more access to admin user.

## Technologies used
### Languages:
* HTML
* CSS
* Python
* JavaScript.

### Tools 
* [GitPod](https://gitpod.io/) for creating the project;
* [GitHub](https://github.com/) for version control;
* [PIP](https://pypi.org/project/pip/) for installation of tools needed in this project;
* [MongoDB Atlas](https://cloud.mongodb.com/) for storing data;
* [Heroku](https://www.heroku.com/) for deployment;
* [Balsamiq](https://balsamiq.com/) was used to create wireframes for the project;
* [Favicon generator](https://www.favicon-generator.org/) was used to generate the favicon;
* [Am I Responsive](http://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.

### Libraries
* [FontAwesome](https://fontawesome.com/) to provide icons;
* [Google Fonts](https://fonts.google.com/) to style website's fonts;
* [JQuery](https://jquery.com/) to simplify DOM manipulation;
* [PyMongo](https://pypi.org/project/pymongo/) to make communication between Python and MongoDB possible;
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) to construct and render pages;
* [Jinja](https://jinja.palletsprojects.com/) to simplify displaying data from the backend of this project smoothly and effectively in html;
* [Materialize](https://materializecss.com/) to simplify the structure of the website and make the website responsive easily.


## Testing
### Testing Using Validators
The website was continuously tested on emulated large and small screens when writing the code. 
Upon completion of the writing process, developer used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/),
[W3C MarkUp Validation Service](https://validator.w3.org/), and [PEP8 online](http://pep8online.com/) to check the validity of the code. 

### Client Stories Testing
Most common path through the website: Home -> Age group -> Book

### Testing on Different Browsers and Devices
The website was tested and proved to be issue-free on the following browsers:
* Chrome;
* Edge;
* Firefox;
* Safari.

The website was also tested on an IOS (Iphone 10) and Android (Pixel 4) platforms. There were detected a few issues, in particular:
* logo in the header wasn't displayed properly;
* display of books and their reviews (book_reviews.html) had some flaws;
* login and register buttons in the unauthorised_error.html were too big;
* profile.html wasn't nicely formatted;
* display of searched books had covers inlined to right;
* social meadia icons were not properly displayed in Safari, while being nice in Chrome;


## How To Run This Project Locally
To clone this project into GitHub, you will need:

A GitHub account. 
* Create your GitHub account [here](https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) 
* Use the Chrome browser.

Then follow these steps:

1. Install the GitPod browser [extentions for Chrome](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki).
1. Restart the browser.
1. Log into [GitPod](https://gitpod.io/workspaces/) using your GitHub account.
1. Navigate to the project GitHub repository.
1. Click the green "GitPod" button in the top right corner.
1. This will trigger a new GitPod workspace to be created from the code in GitHub where you can work locally.

To work on the project code within the local IDE:

1. Navigate to the project GitHub repository.
1. Click "Clone or Download".
1. Copy Clone's URL for the repository.
1. Open the terminal in your local IDE.
1. Change the current working directory to the location where you want the clone directory to be made.
1. Type "git clone" and then paste the URL from the step 3.
1. Press Enter and your local clone will be created.

To run this project, you will need the following to be installed:
1. [pip](https://pypi.org/project/pip/)
1. [Python3](https://realpython.com/installing-python/)
1. an [account at MongoDB Atlas](https://docs.mongodb.com/guides/cloud/account/) or MongoDB running locally on your machine.

## Credits
### Images
Images for the website were downloaded from [Pexels.](https://www.pexels.com/)

### Borrowed Code 
Code for Materialize components, such as buttons, layout, colors, styling etc was taken from 
[Materialize documentation](https://materializecss.com/about.html).
[Stack Overflow website](https://stackoverflow.com/), [W3School tutorials](https://www.w3schools.com/), 
[Slack](https://code-institute-room.slack.com/ssb/redirect?entry_point=homepage_nav) forum, and tutor support
were used when dealing with some specific issues. In particular:
Code for reading data from different collections in MongoDB to create a dictionary of user's reviews was peeked 
[here](https://stackoverflow.com/questions/16849955/how-can-i-join-data-from-two-mongodb-collections-in-python)
However, combining two dictionaries into one was done using new functionality of Python, as seen 
[here](https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-taking-union-of-dictiona) 
Styling of search field in the navbar was inspired by this [post:]
(https://stackoverflow.com/questions/42126743/aligning-search-input-in-navbar-with-materialize)
Custom error page handling was taken from [Flask documentation:] (https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)
Don't allow inputs that start with [white spaces:](https://stackoverflow.com/questions/54020591/not-allow-space-as-a-first-input-character-in-input-field)
Display confirm messages for delete buttons [here:](https://stackoverflow.com/questions/9139075/how-to-show-a-confirm-message-before-delete)
Nicely formatted rows in collapsible [here:](https://github.com/Dogfalo/materialize/issues/3325)