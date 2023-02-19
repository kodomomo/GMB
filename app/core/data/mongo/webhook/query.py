from uuid import UUID

from app.core.data.mongo import CollectionNames, get_collection, Select
from app.core.data.mongo.collections import Webhook


def get_webhook_by_id(id_: UUID):
    collection = get_collection(CollectionNames.WEBHOOK)

    return collection.find_one(
        {Webhook.ID: str(id_)}
    )


def get_secret_by_id(id_: UUID):
    collection = get_collection(CollectionNames.WEBHOOK)

    return collection.find_one(
        {Webhook.ID: str(id_)},
        {Webhook.SECRET: Select.TRUE, Webhook.ID: Select.FALSE}
    )[Webhook.SECRET]
