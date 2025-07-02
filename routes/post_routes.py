from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.db import db

post_bp = Blueprint("post", __name__)

# Create Post
@post_bp.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    author_id = data.get("author_id")

    if not title or not content or not author_id:
        return jsonify({"error": "Title, content and author_id are required"}), 400

    if not ObjectId.is_valid(author_id):
        return jsonify({"error": "Invalid author ID"}), 400

    # check author
    author = db.authors.find_one({"_id": ObjectId(author_id)})
    if not author:
        return jsonify({"error": "Author not found"}), 404

    post = {
        "title": title,
        "content": content,
        "author_id": ObjectId(author_id)
    }
    result = db.posts.insert_one(post)
    return jsonify({"message": "Post created", "post_id": str(result.inserted_id)}), 201

#get post by id
@post_bp.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    if not ObjectId.is_valid(post_id):
        return jsonify({"error": "Invalid post ID"}), 400
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        return jsonify({"error": "Post not found"}), 404

    post["_id"] = str(post["_id"])
    post["author_id"] = str(post["author_id"])
    return jsonify(post)

# update post byid 
@post_bp.route("/posts/<post_id>", methods=["PUT"])
def update_post(post_id):
    if not ObjectId.is_valid(post_id):
        return jsonify({"error": "Invalid post ID"}), 400
    data = request.get_json()
    updated = db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": data})
    if updated.matched_count == 0:
        return jsonify({"error": "Post not found"}), 404
    return jsonify({"message": "Post updated successfully"})

#delete  by id
@post_bp.route("/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    if not ObjectId.is_valid(post_id):
        return jsonify({"error": "Invalid post ID"}), 400
    deleted = db.posts.delete_one({"_id": ObjectId(post_id)})
    if deleted.deleted_count == 0:
        return jsonify({"error": "Post not found"}), 404
    return jsonify({"message": "Post deleted successfully"})

#all data
@post_bp.route("/posts", methods=["GET"])
def get_all_posts():
    posts = []
    for post in db.posts.find():
        post["_id"] = str(post["_id"])       
        post["author_id"] = str(post["author_id"])   
        posts.append(post)
    return jsonify(posts)
