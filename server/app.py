from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


CORS(app)
app.secret_key = "sehtrsdyhndtejdydunuyehbdrvteryhe"

# models
import models

# views
import views.post



# export FLASK_APP=app.py
# export FLASK_DEBUG=1

