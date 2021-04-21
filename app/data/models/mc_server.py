from sqlalchemy import Column, Integer, String, ForeignKey, orm

from app.data.db_session import db


class MCServer(db.Model):
    __tablename__ = "mc_servers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    password = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = orm.relation("User", back_populates="mc_servers")
