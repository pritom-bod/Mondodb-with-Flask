from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.db import db

author_bp = Blueprint("author", __name__)

# create author
@author_bp.route("/authors", methods=["POST"])
def create_author():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Name and Email required"}), 400

    author = {"name": name, "email": email}
    result = db.authors.insert_one(author)
    return jsonify({"message": "Author created", "author_id": str(result.inserted_id)}), 201

# get author by ID
@author_bp.route("/authors/<author_id>", methods=["GET"])
def get_author(author_id):
    if not ObjectId.is_valid(author_id):
        return jsonify({"error": "Invalid author ID"}), 400
    author = db.authors.find_one({"_id": ObjectId(author_id)})
    if not author:
        return jsonify({"error": "Author not found"}), 404
    author["_id"] = str(author["_id"])
    return jsonify(author)

# update author by id
@author_bp.route("/authors/<author_id>", methods=["PUT"])
def update_author(author_id):
    if not ObjectId.is_valid(author_id):
        return jsonify({"error": "Invalid author ID"}), 400
    data = request.get_json()
    updated = db.authors.update_one({"_id": ObjectId(author_id)}, {"$set": data})
    if updated.matched_count == 0:
        return jsonify({"error": "Author not found"}), 404
    return jsonify({"message": "Author updated successfully"})

# delete author by od
@author_bp.route("/authors/<author_id>", methods=["DELETE"])
def delete_author(author_id):
    if not ObjectId.is_valid(author_id):
        return jsonify({"error": "Invalid author ID"}), 400
    deleted = db.authors.delete_one({"_id": ObjectId(author_id)})
    if deleted.deleted_count == 0:
        return jsonify({"error": "Author not found"}), 404
    return jsonify({"message": "Author deleted successfully"})

#all data
@author_bp.route("/authors", methods=["GET"])
def get_all_authors():
    authors = []
    for author in db.authors.find():
        author["_id"] = str(author["_id"])   
        authors.append(author)
    return jsonify(authors)
