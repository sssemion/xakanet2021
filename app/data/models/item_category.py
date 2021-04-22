from sqlalchemy import Column, Integer, String

from app.data.db_session import db


class ItemCategory(db.Model):
    __tablename__ = "item_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
