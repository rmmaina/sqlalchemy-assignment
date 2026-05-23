from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db, migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "test"

CORS(app)

db.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def home():
    return jsonify({"message": "API working"})


# IMPORT BLUEPRINTS (safe now)
from views.user import user_bp
from views.post import post_bp
from views.comment import comment_bp

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)
app.register_blueprint(comment_bp)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)