# project-flask-app
This is a web application that allows users to create their own projects for storing data. It is intended for storing "your favorites" lists, like your favorite books, movies, cars, etc. However, the app can also be used for other things. For example, it might help you compare different products when you are on the verge of buying something. 

This web-based application tries to exploit the benefits of schemaless databases. A nice feature of this app is that you can create your own "columns" in the database. So, you can save and compare on the categories that you think are important. For example, if want to store the IMDB score of your favorite movies you just add it to the project. Another nice feature is that you can store photos and videos. So, you can also store the trailer of the movie.

#### Live demo
A live demo of the web app can be viewed [here].

[here]: https://sdv-flask-app.herokuapp.com/

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
* At the moment the web app is built for personal use. However, by creating login functionality the app could serve multiple users. Each user could have its own account or potentially share projects. Also, when the web app is meant for people other than myself the UX has to be improved. For example, for uploading videos. 

## UX 
People tend to enjoy creating all sorts of "my favorite" lists. For example, favorite books or movies. This web application allows users to create such lists according to what information they want to store. A nice feature of this web application is that the users themselves get to choose what the project categories are. Do they want to store only the author and title of their favorite book? Or also the number of pages, ratings, and book cover photos? Or even book reviews on Youtube?

The application can also help people in the buying decision process. Who doesn't list all the options before buying, for example, a new laptop? This web app lets you do so on the categories that are important for you. 


## Getting started
If you also want to use the web app, you can clone this repo. The following instructions can help you setting up the project on your local machnine. These instructions are for Linux/Mac. Windows might be slightly different. 

#### Prerequisites 
Make sure to install python. Not sure whether you have python? Check by typing ```python --version``` in your terminal. 

#### Installation 
1. Clone the project to your local machine with ```git clone git@github.com:steindevos/project-flask-app.git```. 
2. Create and activate a virtual environment. Create ```$ python3 -m venv ~/virtualenvs/<name_of_environment>``` and activate: ```$ source ~/virtualenvs/<name_of_environment>/bin/activate```. 
3. Pip install the requirments.txt file ```pip3 install -r requirements.txt```. 
4. Link your project with a non-relational database. This project stores data in MongoDB. You can create a free MongoDB database on [Mlab]. 
5. In order to make the project work with your own database change app.py file. Change these lines of code 

```python
app.config["MONGO_DBNAME"] = "flask-app"
app.config["MONGO_URI"] = "mongodb://admin:pa55word10@ds119072.mlab.com:19072/flask-app"
```
Into the following: 
```python
app.config["MONGO_DBNAME"] = <your_deployment_name>
app.config["MONGO_URI"] = "mongodb://<username>:<password>.mlab.com:19072/flask-app"
```

[Mlab]: https://mlab.com/ 
6. Once you have linked to the database you are ready to run the project. Type ```python3 app.py``` in the terminal. You should be able to see the app running on your localhost: ```127.0.0.1:8000```. 

#### Running tests
Once you have the web application up and running you can perform some fuchtional tests. First of all try to create a project and add some cases. If this doesn't work you should check whether you have connected your project to the database properly. 

Also, try to create a two projects with exactly the same name. As a result of the following lines of code this should give an error message on your running website: 

```python
if request.method == "POST":
        project_name = request.form["project"]
        if mongo.db.projects.find_one({"project": project_name}):
            flash("You already have a project titled " + project_name +". Please choose another title.")
            return redirect(url_for("add_project"))
```

This if statement was build in, to prevent bugs. A project that has exactly the same name as another project would leads to cases that are added to the wrong collection in MongoDB. 

Also, try to add a case that doesn't have pictures added to it. When you view the case on the running website there should not be an enourmos blank space. The blank space was created as a result of the empty picture carousel. However, thanks to the following lines of code in the HTML this should be prevented: 

```
{% extends "base.html" %} {% block content%}
{% set ns = namespace(image=false)%}
{%for key, value in case.items() %}{% if key[0:5] == "image"%}{% set ns.image = True %}{% endif%}{% endfor %}
```
```
{% if ns.image %}
<div class="divider"></div>
<div class="carousel carousel-slider">
    {%for key, value in case.items() %} {% if key[0:5] == "image" %}
    <a class="carousel-item" href={{value}}><img src="{{value}}"></a> {% endif%} {%endfor%}
</div>
{% endif %}
```
#### Deployment
If you want to deploy the project on you own Heroku account, you should think of the following: 

* If you have pip installed extra libraries to your own project, make sure to update the requirements.txt file by entering ```pip3 freeze --local > requirements.txt``` in your terminal. Heroku needs this file to install the relevant libraries. 
* Make sure to have the Procfile included in the project. It should have the following line in it: ```web: python app.py```. 
* Add the following config vars to your Heroku settings: 
1. IP - 0.0.0.0
2. PORT - 5000

## Acknowledgements
The styling in the project is mainly done with the help of [MaterializeCSS].

This project could not have been made without the help of all the teachers of the Code Institute! 


[MaterializeCSS]: https://materializecss.com/




