from flask import Blueprint, request, jsonify
from extensions import db
from models import User

user_bp = Blueprint("user_bp", __name__)

print("USER ROUTES LOADED")


# GET ALL USERS
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()

    return jsonify([
        {"id": u.id, "username": u.username}
        for u in users
    ]), 200


# CREATE USER
@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "username is required"}), 400

    new_user = User(username=data["username"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": {"id": new_user.id, "username": new_user.username}
    }), 201


# GET ONE USER
@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = db.session.get(User, id)   # ✅ FIXED (modern SQLAlchemy)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"id": user.id, "username": user.username}), 200


# UPDATE USER
@user_bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = db.session.get(User, id)   # ✅ FIXED

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    user.username = data.get("username", user.username)

    db.session.commit()

    return jsonify({
        "message": "User updated successfully",
        "user": {"id": user.id, "username": user.username}
    }), 200


# DELETE USER
@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.session.get(User, id)   # ✅ FIXED

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200