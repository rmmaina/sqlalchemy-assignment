# Full Stack Blog Application (React + Vite + Flask + SQLAlchemy)

## Overview

This is a full-stack blog application built with a **React (Vite)** frontend and a **Flask REST API backend** using **SQLAlchemy ORM**.

The project demonstrates:
- Frontend development using React + Vite
- Backend API development using Flask
- Relational database design using SQLAlchemy
- Database migrations using Flask-Migrate
- Data seeding using Faker
- Full-stack integration between frontend and backend

---

## Tech Stack

### Frontend
- React
- Vite
- JavaScript (ES6+)
- ESLint

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS
- Faker
- SQLite

---

## Project Structure

project-root/
│
├── client/ # React Frontend (Vite)
│ ├── src/
│ ├── index.html
│ ├── package.json
│ └── vite.config.js
│
├── server/ # Flask Backend
│ ├── app.py # Flask application setup
│ ├── models.py # Database models
│ ├── seed.py # Database seeding script
│ ├── views/ # API routes (Blueprints)
│ ├── migrations/ # Database migrations
│ ├── instance/ # SQLite instance folder
│ └── database.db # SQLite database
│
└── README.md


---

## Features

### Frontend (React + Vite)
- Fast development with Hot Module Replacement (HMR)
- Component-based architecture
- ESLint for code quality
- Modern React setup using Vite plugins

### Backend (Flask API)
- RESTful API structure
- User, Post, and Comment models
- One-to-many relationships
- Database migrations with version control
- Database seeding with realistic fake data
- SQLite lightweight database

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

The `seed.py` script:
- Clears existing data
- Creates 3 users
- Creates 9 posts (distributed among users)
- Creates 1 comment per post
- Uses Faker to generate realistic data

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd project-root

2. Backend Setup (Flask)

cd server

pip install flask flask_sqlalchemy flask_migrate flask_cors faker

#Initialize Database

flask db init
flask db migrate -m "initial migration"
flask db upgrade

#Seed Database

python seed.py

#Run Backend Server
python app.py

#3. Frontend Setup (React + Vite)
cd client
npm install
npm run dev

#Expected Output After seeding the database:

3 users created
9 posts created
9 comments created

#API Concepts Demonstrated
REST API design
CRUD operations
Flask Blueprints
JSON responses
Database relationships (One-to-Many)

#React + Vite Notes
This frontend uses the default Vite React template:
  Fast Refresh (HMR)
  ESLint rules enabled
  Optional React Compiler support

#Key Concepts Demonstrated
  Full-stack architecture (React + Flask)
  ORM database modeling (SQLAlchemy)
  Backend API development
  Frontend tooling with Vite
  Database migrations and version control
  Data seeding with Faker

#Author
Robert Maina

