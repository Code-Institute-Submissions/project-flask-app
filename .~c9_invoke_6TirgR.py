import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "flask-app"
app.config["MONGO_URI"] = "mongodb://admin:pa55word10@ds119072.mlab.com:19072/flask-app"
mongo = PyMongo(app)

@app.route("/")
def show_index():
    return render_template("index.html", topics=mongo.db.topics.find())

@app.route("/add", methods=["GET", "POST"])
def add_topic():
    if request.method == "POST":
        topics = mongo.db.topics
        topics.insert_one(request.form.to_dict())
        return redirect("/")
    
    return render_template("addtopic.html")
    
@app.route("/case/<topic_id>/<topic_name>")
def show_cases(topic_id, topic_name):
    dbname = topic_name
    coll = mongo.db[dbname]
    return render_template("showcases.html", cases=coll.find(), cases_title=dbname, topic_id=topic_id)


@app.route("/case/<topic_id>/<topic_title>/add", methods=["GET", "POST"])
def add_case(topic_id, topic_title):
    if request.method == "POST":
        coll = mongo.db[topic_title]
        coll.insert_one(request.form.to_dict())
        return redirect("/case/"+topic_id+"/"+topic_title)
    topic = mongo.db.topics.find_one({"_id": ObjectId(topic_id)})
    return render_template("addcase.html", case=topic)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True
    )