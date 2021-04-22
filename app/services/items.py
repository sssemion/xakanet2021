from app.data.db_session import create_session
from app.data.models import Item, ItemCategory


def get_all_items_json():
    with create_session() as session:
        data = dict()
        categories = session.query(ItemCategory).all()
        for category in categories:
            data[category.name] = [
                {**item.to_dict(only=["id", "name", "price"]), "photo": get_photo_filename(item.name, category.name)}
                for item in session.query(Item).filter(Item.category_id == category.id).all()]
    return data


def get_photo_filename(name, category_name):
    return category_name + "/" + "_".join(name.title().split()) + ".png"
