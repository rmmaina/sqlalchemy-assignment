from extensions import db
from sqlalchemy_serializer import SerializerMixin


# USER MODEL
class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    serialize_rules = (
        '-posts.user',
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        nullable=False
    )

    # RELATIONSHIP
    posts = db.relationship(
        "Post",
        backref='user',
        cascade="all, delete-orphan"
    )


# POST MODEL
class Post(db.Model, SerializerMixin):

    __tablename__ = "posts"

    serialize_rules = (
        '-user.posts',
        '-comments.post',
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    # RELATIONSHIP
    comments = db.relationship(
        "Comment",
        backref='post',
        cascade="all, delete-orphan"
    )


# COMMENT MODEL
class Comment(db.Model, SerializerMixin):

    __tablename__ = "comments"

    serialize_rules = (
        '-post.comments',
    )

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey("posts.id")
    )