from datetime import datetime
from uuid import UUID


class PendingWebhook(dict):
    ID = '_id'
    SECRET = 'secret'
    SENDER_ID = 'senderId'
    CREATED_AT = 'createdAt'

    def __init__(
            self,
            secret: str,
            sender_id: str,
            id_: UUID,
            created_at: datetime  # ttl works when date type is utc
    ):
        super().__init__(
            _id=str(id_),
            secret=secret,
            senderId=sender_id,
            createdAt=created_at
        )