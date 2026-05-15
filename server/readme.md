Flask SQLAlchemy Assignment
Overview

This project is a Flask application that uses SQLAlchemy ORM to manage a simple database system consisting of Users, Posts, and Comments. It demonstrates database modeling, relationships, and data seeding.

Technologies Used
Python
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite
Faker
Project Structure
server/
│
├── app.py              # Flask application setup
├── models.py           # Database models
├── seed.py             # Database seeding script
├── views/              # Application routes
├── migrations/         # Migration files
├── instance/
└── database.db         # SQLite database file
Database Models
User
id (Primary Key)
username (String)

Relationships:

One user has many posts
Post
id (Primary Key)
title (String)
content (Text)
user_id (Foreign Key)

Relationships:

Belongs to a user
Has many comments
Comment
id (Primary Key)
message (Text)
post_id (Foreign Key)

Relationships:

Belongs to a post
Database Seeding

The seed.py script performs the following:

Deletes existing data from all tables
Creates 3 users
Creates 9 posts (distributed among users)
Creates 1 comment per post
Uses Faker to generate sample data

How to Run the Project
1. Install dependencies
pip install flask flask_sqlalchemy flask_migrate flask_cors faker
2. Initialize database migrations (if needed)
flask db init
flask db migrate
flask db upgrade
3. Run the seed script
python seed.py

Expected Output After Seeding
 3 users created
 9 posts created
 9 comments created

Setup Instructions

Clone the repository
Navigate to the project folder
Install dependencies
Run migrations
Seed the database


Author
Robert Maina
