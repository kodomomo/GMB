from uuid import UUID

from app.core.data.mongo import get_collection
from app.core.data.mongo.collections import CollectionNames


def get_page_access_token():
    collection = get_collection(CollectionNames.TOKEN)

    return collection.find_one()['_id']


def get_pending_webhook(id_: UUID):
    collection = get_collection(CollectionNames.PENDING_WEBHOOK) # TODO
    return collection.find(
        {'_id': str(id_)},
    )
