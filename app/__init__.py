import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager

from app.data import db_session

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError(".env file not found")

app = Flask(__name__)
pg_user = os.environ.get("PG_USER")
pg_pass = os.environ.get("PG_PASS")
pg_host = os.environ.get("PG_HOST")
db_name = os.environ.get("DB_NAME")

app.config["SECRET_KEY"] = os.environ.get("APP_SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgres://{pg_user}:{pg_pass}@{pg_host}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = db_session.global_init()
db.init_app(app)

login_manager = LoginManager(app)

from app import controllers
