from uuid import UUID

from app.core.data.mongo import get_collection
from app.core.data.mongo.collections import CollectionNames, PendingWebhook


def get_pending_webhook(id_: UUID):
    collection = get_collection(CollectionNames.PENDING_WEBHOOK) # TODO
    return collection.find_one(
        {PendingWebhook.ID: str(id_)},
    )


def get_pending_webhook_and_delete(id_: UUID):
    collection = get_collection(CollectionNames.PENDING_WEBHOOK)

    return collection.find_one_and_delete(
        {PendingWebhook.ID: str(id_)}
    )
