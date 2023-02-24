from uuid import UUID

from app.common.exception import throw
from app.common.exception.webhook import WebhookNotFoundException
from app.core.data.mongo import CollectionNames, get_collection, Select
from app.core.data.mongo.webhook import Webhook


def get_webhook_by_id(id_: UUID):
    collection = get_collection(CollectionNames.WEBHOOK)

    return v \
        if \
        (
            v := collection.find_one(
                {
                    Webhook.ID: str(id_)
                }
            )
        ) is not None \
        else throw(WebhookNotFoundException)


def get_secret_by_id(id_: UUID):
    collection = get_collection(CollectionNames.WEBHOOK)

    return collection.find_one(
        {Webhook.ID: str(id_)},
        {Webhook.SECRET: Select.TRUE, Webhook.ID: Select.FALSE}
    )[Webhook.SECRET]
