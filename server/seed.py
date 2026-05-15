from faker import Faker

from app import app, db
from models import Comment, Post, User

fake = Faker()

with app.app_context():

    # -------------------------
    # CLEAR TABLES
    # -------------------------
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()
    db.session.commit()

    # -------------------------
    # CREATE USERS (3)
    # -------------------------
    users = [User(username=fake.unique.user_name()) for _ in range(3)]
    db.session.add_all(users)
    db.session.flush()

    # -------------------------
    # CREATE POSTS (9)
    # -------------------------
    posts = [
        Post(
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=5),
            user_id=users[index % len(users)].id,
        )
        for index in range(9)
    ]

    db.session.add_all(posts)
    db.session.flush()

    # -------------------------
    # CREATE COMMENTS (1 per post)
    # -------------------------
    comments = [
        Comment(
            message=fake.sentence(nb_words=12),
            post_id=post.id
        )
        for post in posts
    ]

    db.session.add_all(comments)
    db.session.commit()

    # -------------------------
    # VERIFY
    # -------------------------
    print("\nUsers:", len(User.query.all()))
    print("Posts:", len(Post.query.all()))
    print("Comments:", len(Comment.query.all()))

    print("\n✅ Seed completed successfully!")