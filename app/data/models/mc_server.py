from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy_serializer import SerializerMixin

from app.data.db_session import db


class MCServer(db.Model, SerializerMixin):
    __tablename__ = "mc_servers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    host = Column(String, nullable=False)
    rcon_port = Column(Integer, nullable=False)
    rcon_password = Column(String, nullable=False)
    nickname = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = orm.relation("User", foreign_keys=[owner_id], back_populates="mc_servers")

    def to_dict(self, additional=None, *args, **kwargs):
        if additional is None:
            additional = []
        if "only" in kwargs:
            return super(MCServer, self).to_dict(*args, **kwargs)
        res = super(MCServer, self).to_dict(only=["id", "name", "host", "rcon_port", "rcon_password",
                                                  "nickname", "owner"])
        for k, v in super(MCServer, self).to_dict(only=additional).items():
            res[k] = v
        return res
