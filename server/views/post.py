from flask import Blueprint, request, jsonify
from extensions import db
from models import Post

post_bp = Blueprint("post_bp", __name__)

print("POST ROUTES LOADED")


@post_bp.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()

    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "content": p.content
        } for p in posts
    ]), 200


@post_bp.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()

    new_post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"]
    )

    db.session.add(new_post)
    db.session.commit()

    return jsonify({"message": "Post created"}), 201


@post_bp.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({
        "id": post.id,
        "title": post.title,
        "content": post.content
    }), 200


@post_bp.route("/posts/<int:id>", methods=["PUT"])
def update_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()

    post.title = data.get("title", post.title)
    post.content = data.get("content", post.content)

    db.session.commit()

    return jsonify({"message": "Post updated"}), 200


@post_bp.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(id):
    post = Post.query.get(id)

    if not post:
        return jsonify({"error": "Post not found"}), 404

    db.session.delete(post)
    db.session.commit()

    return jsonify({"message": "Post deleted"}), 200