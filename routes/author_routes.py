from flask import Blueprint, render_template, request, redirect, url_for
from bson import ObjectId
from utils.db import db

author_bp = Blueprint("author", __name__)

# list
@author_bp.route("/authors")
def list_authors():
    authors = list(db.authors.find())
    for a in authors:
        a["_id"] = str(a["_id"])
    return render_template("authors/list.html", authors=authors)

# create
@author_bp.route("/authors/create", methods=["GET", "POST"])
def create_author():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        db.authors.insert_one({"name": name, "email": email})
        return redirect(url_for("author.list_authors"))
    return render_template("authors/create.html")

# edit
@author_bp.route("/authors/edit/<author_id>", methods=["GET", "POST"])
def edit_author(author_id):
    author = db.authors.find_one({"_id": ObjectId(author_id)})
    if not author:
        return "Author not found", 404
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        db.authors.update_one({"_id": ObjectId(author_id)}, {"$set": {"name": name, "email": email}})
        return redirect(url_for("author.list_authors"))
    author["_id"] = str(author["_id"])
    return render_template("authors/edit.html", author=author)

# delete
@author_bp.route("/authors/delete/<author_id>")
def delete_author(author_id):
    db.authors.delete_one({"_id": ObjectId(author_id)})
    return redirect(url_for("author.list_authors"))
