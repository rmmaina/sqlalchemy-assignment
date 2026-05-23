from flask import Blueprint, request, jsonify
from extensions import db
from models import Comment, Post

comment_bp = Blueprint("comment_bp", __name__)

print("COMMENT ROUTES LOADED")


@comment_bp.route("/comments", methods=["GET"])
def get_comments():
    comments = Comment.query.all()

    return jsonify([
        {
            "id": c.id,
            "message": c.message,
            "post_id": c.post_id
        } for c in comments
    ]), 200


@comment_bp.route("/comments", methods=["POST"])
def create_comment():
    data = request.get_json()

    if not data or "post_id" not in data or "message" not in data:
        return jsonify({"error": "post_id and message are required"}), 400

    post = db.session.get(Post, data["post_id"])
    if not post:
        return jsonify({"error": "Post not found"}), 404

    new_comment = Comment(
        message=data["message"],
        post_id=data["post_id"]
    )

    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"message": "Comment created"}), 201


@comment_bp.route("/comments/<int:id>", methods=["GET"])
def get_comment(id):
    comment = db.session.get(Comment, id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    return jsonify({
        "id": comment.id,
        "message": comment.message,
        "post_id": comment.post_id
    }), 200


@comment_bp.route("/comments/<int:id>", methods=["PUT"])
def update_comment(id):
    comment = db.session.get(Comment, id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    comment.message = data.get("message", comment.message)

    db.session.commit()

    return jsonify({"message": "Comment updated"}), 200


@comment_bp.route("/comments/<int:id>", methods=["DELETE"])
def delete_comment(id):
    comment = db.session.get(Comment, id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "Comment deleted"}), 200