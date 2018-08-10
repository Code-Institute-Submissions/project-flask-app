import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "flask-app"
app.config["MONGO_URI"] = "mongodb://admin:pa55word10@ds119072.mlab.com:19072/flask-app"
mongo = PyMongo(app)

@app.route("/")
def show_index():
    return render_template("index.html")

@app.route("/add")
def addtopic():
    return render_template("addtopic.html")



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True
    )