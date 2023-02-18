from uuid import uuid4

from app.util.time import utc_now

from app.core.data.mongo import (
    get_collection,
    CollectionNames,
    PendingWebhook
)


def create_pending_webhook(secret: str, sender_id: str):
    collection = get_collection(CollectionNames.PENDING_WEBHOOK)

    collection.insert_one(
        PendingWebhook(
            id_=uuid4(),
            secret=secret,
            sender_id=sender_id,
            created_at=utc_now()
        )
    )
