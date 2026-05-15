# Flask SQLAlchemy Blog API

## Overview
This project is a Flask-based backend application built using SQLAlchemy ORM. It demonstrates relational database design, model relationships, and database seeding using Faker.

The system models a simple blog structure with Users, Posts, and Comments.

---

## Features
- User, Post, and Comment models
- One-to-many relationships
- Database seeding with realistic fake data
- Flask-Migrate integration for database versioning
- SQLite database for storage

---

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Faker

---

## Project Structure


server/
│
├── app.py # Flask application setup
├── models.py # Database models
├── seed.py # Database seeding script
├── views/ # Application routes
├── migrations/ # Database migrations
├── instance/
└── database.db # SQLite database file


---

## Database Design

### User
- id (Primary Key)
- username (String)

**Relationships:**
- A user can create multiple posts

---

### Post
- id (Primary Key)
- title (String)
- content (Text)
- user_id (Foreign Key → User.id)

**Relationships:**
- Belongs to a user
- Has multiple comments

---

### Comment
- id (Primary Key)
- message (Text)
- post_id (Foreign Key → Post.id)

**Relationships:**
- Belongs to a post

---

## Database Seeding

The `seed.py` script performs the following operations:

- Clears existing database records
- Creates 3 users
- Creates 9 posts (distributed among users)
- Creates 1 comment per post
- Uses Faker to generate realistic sample data

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd server
2. Install dependencies
pip install flask flask_sqlalchemy flask_migrate flask_cors faker
3. Initialize database migrations
flask db init
flask db migrate
flask db upgrade
4. Seed the database
python seed.py
Expected Output

After running the seed script:

3 users created
9 posts created
9 comments created
Key Concepts Demonstrated
Flask application architecture
SQLAlchemy ORM relationships
Database normalization
One-to-many relationship mapping
Data seeding with Faker
Flask-Migrate workflow
Author

Robert Maina