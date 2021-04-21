import datetime

from flask_login import UserMixin
from sqlalchemy import Integer, Column, String, DateTime, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from app.data.db_session import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    username = Column(String(32), nullable=False, unique=True, index=True)

    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    password = Column(String, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
