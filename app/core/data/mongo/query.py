from app.core.data.mongo import get_collection
from app.core.data.mongo.collections import CollectionNames


def get_page_access_token():
    collection = get_collection(CollectionNames.TOKEN)

    return collection.find_one()['_id']
