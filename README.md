# Read to me
![responsive website](https://github.com/irasan/read-to-me/blob/master/static/images/read-me-responsive.png)

This is a web service that allows its users to find the best childrens books, based on reviews and ratings of other users. 
There are thousands of books out there and while many of them might seem appealing or beautifully illustrated to adults, they are not 
necessarily insteresting for children. Also people tend to buy books that are famous and popular, leaving a small chance for short run 
or other great books to be found. That's why this service will gather feedback on books from the point of view of the child. 

Books are categorised according to 4 age groups:
1. 0-2 years old: here users will find books with no or very little text as well as first nursery rhymes;
1. 3-5 years old: beautifully illustrated books with short stories and poems. Cartoon characters and first interests can also 
be found here;
1. 6-8 years old: books for children that start reading themselves as well as books with long stories where accent is on the
text, not the illustrations;
1. 9-12 years old: this category will contain adventure books and other fascinating stories that promote reading.

## UX

### Project goals
The primary goal of the project is to present a collection of favourite children’s books and help users to make easier decisions when 
purchasing new books. 

### Customers' goals
The main audience for this website consists of yound parents and grandparents who would like to promote reading in their homes.
Their main goal would be to find great books for children to read, to share their experiences regarding books they've read, as well as
save money and help other people to do so by preventing from investing in beautiful but not so interesting books.

Customers goals are:
* find best books according to children’s age group;
* find best books according to children’s interests;
* share feedback on books from the point of view of their children;
* see a list of his/her reviews and ratings;
* be able to update his/her reviews and ratings;
* be able to create a list of books to read and update it.

This website helps the users to meet their needs because: 
* the goals stated above were taken into consideration during all stages of the development process;
* users can register their profiles, create reviews on books and rate them;
* registered users can see a list of their reviews and ratings;
* registered users can create books-to-read lists;
* navigation is traditional and intuitive.

### Developer's Goals
This is a learning project and the main purpose of it's creating is to learn Python and how to connect a database to
the project. Another very improtant goal is to build a game that will be added to the portfolio. 

### User Stories
As a young parent/grandparent, I want:
* to cultivate love to books and promote reading for my kids, that's why I need to find the best books;
* to buy books that are loved by modern children and are not simply a tribute to traditions or best promoted;
* to create a list of great books and update it when I bought something or am no longer interested;
* to share my thoughts about books that were read to my children and help other parents to make a decision.

As a reading child I want:
* to make use of a service like goodreads.com only for children and by like-minded children;
* to share my feedback on books and be able to read feedback of other children.

### Wireframes
After thorough consideration of users' and developer's goals, the following [wireframes](static/images/wireframes) were created. 

### Design Choices
The overall feel of the website is simple, happy, and inviting. The following design choices were made in order to implement the game: 

#### Fonts
Josefin Slab was chosen as main font for the website. It features round, a bit Gothic letters and reminds fonts in children's books.
Logo was written with Gloria Hallelujah. This is fun, comic-like font based on handwriting and very easy to read. 
Both fonts were downloaded from [Google Fonts.](https://fonts.google.com/)

#### Icons
All icons were chosen for their obvious meaning so that they can be easily understood by everyone. Icons were implemented 
using [Font Awesome.](https://fontawesome.com/)
Smiley faces for different ratings were downloaded from [here:](https://www.flaticon.com/packs/classics-2?word=emoji)

#### Colors and Styling
Color palette for this project was created using [Coolors.co](https://coolors.co) service.
It is recommended to choose bold and bright colors for children. Keeping in mind gender neutrality, the following were picked
for the project:
![color pallette](https://github.com/irasan/read-to-me/blob/master/static/images/colors.png)
During implementation of the project, in order to simplify it, all colors except the main background color were picked from those
available on [Materialize.](https://materializecss.com/color.html), but closely matching the palette.

Overall design of the website is cheerful, bright, and playful in order to highlight it's purpose and audience.

## Features
This website features a few pages which are visible or not depending on the type of user. In particular, visitors of the site who 
hasn't registered or logged in, will be able to see Home page with books divided by different age categories, lists of books in every age group,
and each individual book together with it's reviews. They will also be able to login or register.
Registered and logged in users will see two additional tabs: My reviews, featuring all the reviews they made, and Add Review.
Admin user, apart from the functionality mentioned above, will be able to manage book categories, add new, update, and delete them.

Many pages feature a sticky floating call-to-action buttons that allow to add reviews.

All pages are connected with each other, passing parameters and creating better UX. Particularly, if users click on the add review 
button from the home page(choosing an age group) or book page (in order to leave review on this particular book), the form temlate
will be pre-filled automatically with the key values (age, book title or book author).

### Existing Features
* User registration and login - supported by MongoDB;
* Functionality to add new books and reviews on them;
* Possibility to change and delete reviews;
* Books can be distinquished by different age groups and categories;
* Books have covers stored in a separate collection;
* Each book will be displayed with it's average rating based on all the reviews that were left on this book;
* Beside ratings users will find smiley faces, that change according to the rating from sad to very happy;
* Call for action buttons - helps users to take control over when to start playing and navigate the site;
* FUnctionality to add, update, and delete book categories for admin user.

### Features Left To implement
* Possibility to sort books according to their ratings or categories;
* Partial search.

## Technologies used
During completion of this project mainly HTML, CSS and Python were used. The project also made use of Flask and Materialize frameworks.
All data is stored in MongoDB, while deployment is supported by Heroku. To create the project, in particular 
write the code itself and store it, GitPod and GitHub were used.

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
1. Type "git clone" and then paste the URK from the step 3.
1. Press Enter and your local clone will be created.

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