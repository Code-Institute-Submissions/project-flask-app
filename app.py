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
    
@app.route("/project/<project_name>")
def show_cases(project_name):
    project = mongo.db.projects.find_one({"project": project_name})
    dbname = project['project']
    coll = mongo.db[dbname]
    return render_template("showcases.html", cases=coll.find(), cases_title=dbname, project=project)
    
@app.route("/showcase/<project_title>/<case_id>")
def show_single_case(project_title, case_id):
    coll = mongo.db[project_title]
    case = coll.find_one({"_id": ObjectId(case_id)})
    return render_template("showsinglecase.html", case=case)

@app.route("/editcase/<project_title>/<case_id>", methods=["GET", "POST"])
def edit_single_case(project_title, case_id):
    if request.method == "POST":
        coll = mongo.db[project_title]
        coll.update({"_id": ObjectId(case_id)}, request.form.to_dict())
        return redirect(url_for("show_cases", project_name=project_title))
    coll = mongo.db[project_title]
    case = coll.find_one({"_id": ObjectId(case_id)})
    return render_template("editsinglecase.html", case=case)

@app.route("/project/<project_title>/add", methods=["GET", "POST"])
def add_case(project_title):
    if request.method == "POST":
        coll = mongo.db[project_title]
        coll.insert_one(request.form.to_dict())
        return redirect(url_for("show_cases", project_name=project_title))
    project = mongo.db.projects.find_one({"project":project_title})
    return render_template("addcase.html", case=project)

@app.route("/edit/<project_id>", methods=["POST", "GET"])
def edit_project(project_id):
    if request.method == "POST":
        mongo.db.projects.update({"_id":ObjectId(project_id)}, request.form.to_dict())
        return redirect(url_for("show_index"))
    project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    return render_template("editproject.html", project=project)

@app.route("/project/<project_id>/<project_title>/delete", methods=["POST"])
def delete_project(project_id, project_title):
    mongo.db.projects.remove({"_id": ObjectId(project_id)})
    mongo.db.drop_collection(project_title)
    return redirect(url_for("show_index"))

@app.route("/deletecase/<project_title>/<case_id>", methods=["POST"])
def delete_case(project_title, case_id):
    coll = mongo.db[project_title]
    coll.remove({"_id": ObjectId(case_id)})
    return redirect(url_for("show_cases", project_name=project_title))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True
    )
    
