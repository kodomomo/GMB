from app.core.data.mongo import CollectionNames, get_collection
from app.core.data.mongo.token import MessengerToken


def get_page_access_token():
    collection = get_collection(CollectionNames.TOKEN)

    return collection.find_one()[MessengerToken.TOKEN]
