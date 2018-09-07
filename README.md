# project-flask-app
This is a web application that allows users to create their own projects for storing data. It is intended for storing "your favorites" lists, like your favorite books, movies, cars, etc. However, the app can also be used for other things. For example, it might help you compare different products when you are on the verge of buying something. 
A nice feature of this app is that you can create your own "columns" in the database. So, you can save and compare on the categories that you think are important. For example, if want to store the IMDB score of your favorite movies you just add it to the project. Another nice feature is that you can store photos and videos. So, you can also store the trailer of the movie.

#### Live demo
A live demo of the web app can be viewed here. 

## Built with
1. Flask
2. HTML5
3. CSS3
4. Python
5. JavaScript
6. JQuery
7. MaterializeCSS
8. MongoDB

## Features
* Create project - A user can create project and determine what information should be stored in the database.
* Add cases to the project - After creating a projects the user can add as many cases to the project as he or she wants. 
* Add media - Images and videos can also be added

###### Features left to implement: 
* At the moment the web app is built for personal use. However, by creating login functionality the app could serve multiple users. Each user could have its own account or potentially share projects. 

## UX 
People tend to enjoy creating all sorts of "my favorite" lists. For example, favorite books or movies. This web application allows users to create such lists according to what information they want to store. A nice feature of this web application is that the users themselves get to choose what the project categories are. Do they want to store only the author and title of their favorite book? Or also the number of pages, ratings, and book cover photos? Or even book reviews on Youtube? 
The application can also help people in the buying decision process. Who doesn't list all the options before buying, for example, a new laptop? This web app lets you do so on the categories that are important for you. 

## Getting started
If you also want to use the web app, you can clone this repo. The following instructions can help you setting up the project on your local machnine. These instructions are for Linux/Mac. Windows might be slightly different. 

#### Prerequisites 
Make sure to install python. Not sure whether you have python? Check by typing ```python --version``` in your terminal. 

#### Installation 
1. Clone the project to your local machine with ```git clone git@github.com:steindevos/project-flask-app.git```. 
2. Create and activat a virtual environment. Create ```$ python3 -m venv ~/virtualenvs/<name_of_environment> and activate: $ source ~/virtualenvs/<name_of_environment>/bin/activate```. 
3. Pip install the requirments.txt file ```pip3 install -r requirements.txt```. 
4. Link your project with a non-relational database. This project stores data in MongoDB. You can create a free MongoDB database on [Mlab]. 
5. In order to make the project work with your own database change app.py file. Change these lines of code 

```python
app.config["MONGO_DBNAME"] = "flask-app"
app.config["MONGO_URI"] = "mongodb://admin:pa55word10@ds119072.mlab.com:19072/flask-app"
```
Into 
```python
app.config["MONGO_DBNAME"] = <your_deployment_name>
app.config["MONGO_URI"] = "mongodb://<username>:<password>.mlab.com:19072/flask-app"
```

[Mlab]: https://mlab.com/ 
6. How to run the project? aegghjmm mbv

