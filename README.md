# Read to me
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
After thorough consideration of users' and developer's goals, the following [wireframes](assets/wireframes) were created. 

### Design Choices

#### Fonts

#### Icons

#### Colors and Styling

### Borrowed Code 
Code for reading data from different collections in MongoDB to create a dictionary of user's reviews was peeked 
[here](https://stackoverflow.com/questions/16849955/how-can-i-join-data-from-two-mongodb-collections-in-python)
However, combining two dictionaries into one was done using new functionality of Python, as seen 
[here](https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-taking-union-of-dictiona) 
Styling of search field in the navbar was inspired by this [post:]
(https://stackoverflow.com/questions/42126743/aligning-search-input-in-navbar-with-materialize)