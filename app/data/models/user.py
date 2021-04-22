import datetime

from flask_login import UserMixin
from sqlalchemy import Integer, Column, String, DateTime, Boolean, orm, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.data.db_session import db
from app.data.models.mc_server import MCServer


class User(db.Model, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True, index=True)
    username = Column(String(32), nullable=False, unique=True, index=True)

    creation_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    password = Column(String, nullable=False)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmation_code = Column(Integer, nullable=True)

    youtube = Column(String, nullable=True)
    twitch = Column(String, nullable=True)

    photo = Column(String, nullable=True)

    active_mc_server = Column(Integer, ForeignKey("mc_servers.id"))
    mc_servers = orm.relation("MCServer", back_populates="owner", primaryjoin=id == MCServer.owner_id, lazy="dynamic")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __eq__(self, other):
        try:
            return self.id == other.id
        except AttributeError:
            return False

    def to_dict(self, additional=None, *args, **kwargs):
        if additional is None:
            additional = []
        if "only" in kwargs:
            return super(User, self).to_dict(*args, **kwargs)
        res = super(User, self).to_dict(only=["id", "username", "creation_date", "youtube", "twitch", "photo"])
        if "mc_servers" in additional:
            res["mc_servers"] = [server.to_dict(only=["id", "name", "host", "rcon_port", "rcon_password", "nickname"])
                                 for server in self.mc_servers]
            additional.remove("mc_servers")
        if additional:
            for k, v in super(User, self).to_dict(only=additional).items():
                res[k] = v
        return res
