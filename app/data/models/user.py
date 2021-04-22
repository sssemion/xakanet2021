import datetime

from flask_login import UserMixin
from sqlalchemy import Integer, Column, String, DateTime, Boolean, orm, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.data.db_session import db
from app.data.models.mc_server import MCServer


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    username = Column(String(32), nullable=False, unique=True, index=True)

    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    password = Column(String, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)

    active_mc_server = Column(Integer, ForeignKey("mc_servers.id"))
    mc_servers = orm.relation("MCServer", back_populates="owner", primaryjoin=id == MCServer.owner_id, lazy="dynamic")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
