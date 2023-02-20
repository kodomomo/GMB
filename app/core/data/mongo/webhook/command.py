from uuid import UUID
from datetime import datetime

from app.core.data.mongo import get_collection
from app.core.data.mongo.collections import CollectionNames
from app.core.data.mongo.pending_webhook import PendingWebhook
from app.core.data.mongo.webhook import Webhook, User, Repository
from app.util.time import ktc_now


def create_webhook(
        id_: UUID,
        secret: str,
        user: User,
        repository: Repository,
):
    collection = get_collection(CollectionNames.WEBHOOK)

    collection.insert_one(
        Webhook(
            id_=id_,
            secret=secret,
            created_at=ktc_now(),
            user=user,
            repository=repository,
            event_amt=0,
        )
    )
