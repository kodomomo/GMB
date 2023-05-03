from uuid import UUID, uuid4
from datetime import datetime

import pymongo
from pydantic import Field
from beanie import Document, Indexed


class PendingWebhook(Document):
    id: UUID = Field(default_factory=uuid4)
    secret: str
    sender_id: str

    created_at: datetime = Indexed(
        datetime, pymongo.ASCENDING, expireAfterSeconds=100,
    )

