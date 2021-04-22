from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy_serializer import SerializerMixin

from app.data.db_session import db


class Item(db.Model, SerializerMixin):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    category_id = Column(Integer, ForeignKey("item_categories.id"), nullable=False)
    category = orm.relation("ItemCategory", foreign_keys=[category_id])
