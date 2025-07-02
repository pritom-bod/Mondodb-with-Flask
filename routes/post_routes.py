from flask import Blueprint, render_template, request, redirect, url_for
from bson import ObjectId
from utils.db import db

post_bp = Blueprint("post", __name__)

# list
@post_bp.route("/posts")
def list_posts():
    posts = list(db.posts.find())
    authors = {str(a["_id"]): a["name"] for a in db.authors.find()}
    for p in posts:
        p["_id"] = str(p["_id"])
        p["author_id"] = str(p["author_id"])
        p["author_name"] = authors.get(p["author_id"], "Unknown")
    return render_template("posts/list.html", posts=posts)

# create
@post_bp.route("/posts/create", methods=["GET", "POST"])
def create_post():
    authors = list(db.authors.find())
    for a in authors:
        a["_id"] = str(a["_id"])
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author_id = request.form["author_id"]
        db.posts.insert_one({"title": title, "content": content, "author_id": ObjectId(author_id)})
        return redirect(url_for("post.list_posts"))
    return render_template("posts/create.html", authors=authors)

# edit
@post_bp.route("/posts/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        return "Post not found", 404
    authors = list(db.authors.find())
    for a in authors:
        a["_id"] = str(a["_id"])
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author_id = request.form["author_id"]
        db.posts.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": {"title": title, "content": content, "author_id": ObjectId(author_id)}}
        )
        return redirect(url_for("post.list_posts"))
    post["_id"] = str(post["_id"])
    post["author_id"] = str(post["author_id"])
    return render_template("posts/edit.html", post=post, authors=authors)

# delete
@post_bp.route("/posts/delete/<post_id>")
def delete_post(post_id):
    db.posts.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for("post.list_posts"))
