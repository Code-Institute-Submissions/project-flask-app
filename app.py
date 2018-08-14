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
    return render_template("index.html", projects=mongo.db.projects.find())

@app.route("/add", methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        projects = mongo.db.projects
        projects.insert_one(request.form.to_dict())
        return redirect("/")
    
    return render_template("addproject.html")
    
@app.route("/case/<project_id>/<project_name>")
def show_cases(project_id, project_name):
    dbname = project_name
    coll = mongo.db[dbname]
    return render_template("showcases.html", cases=coll.find(), cases_title=dbname, project_id=project_id)


@app.route("/case/<project_id>/<project_title>/add", methods=["GET", "POST"])
def add_case(project_id, project_title):
    if request.method == "POST":
        coll = mongo.db[project_title]
        coll.insert_one(request.form.to_dict())
        return redirect("/case/"+project_id+"/"+project_title)
    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    return render_template("addcase.html", case=project)




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True
    )