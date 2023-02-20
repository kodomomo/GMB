from typing import Optional
from uuid import UUID

from app.core.data.mongo import get_collection
from app.core.data.mongo.collections import CollectionNames
from app.core.data.mongo.webhook import Webhook, User, Repository, Amt
from app.util.time import ktc_now


def create_webhook(
        id_: UUID,
        secret: str,
        user: User,
        repository: Repository,
        amt: Optional[Amt] = Amt(0, 0, 0, 0)
):
    collection = get_collection(CollectionNames.WEBHOOK)

    collection.insert_one(
        Webhook(
            id_=id_,
            secret=secret,
            created_at=ktc_now(),
            user=user,
            repository=repository,
            amt=amt
        )
    )


def update_amt(
        id_: UUID,
        amt_type: str
):
    collection = get_collection(CollectionNames.WEBHOOK)

    collection.update_one(
        {Webhook.ID: str(id_)},
        {'$inc': {amt_type: 1}}
    )
