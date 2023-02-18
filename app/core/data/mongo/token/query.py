from app.core.data.mongo import CollectionNames, get_collection


def get_page_access_token():
    collection = get_collection(CollectionNames.TOKEN)

    return collection.find_one()['_id']
