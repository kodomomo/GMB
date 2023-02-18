from uuid import UUID, uuid4
from typing import Optional, List
from datetime import datetime

from app.util.time import utc_now, ktc_now


class CollectionNames:
    TOKEN = 'messengerToken'
    WEBHOOK_USER = 'webhookUser'
    PENDING_WEBHOOK = 'pendingWebhook'
    WEBHOOK = 'webhook'
    REPOSITORY = 'repository'

    NAME_LIST = [TOKEN, WEBHOOK, PENDING_WEBHOOK]


class MessengerToken(dict):
    TOKEN = 'token'

    def __init__(
            self,
            token: str
    ):
        super().__init__(
            _id=token
        )


class WebhookUser(dict):
    GITHUB_ID = 'githubId'
    GITHUB_NAME = 'githubName'
    SENDER_ID = 'senderId'

    def __init__(
            self,
            github_id: str,
            github_name: str,
            sender_id: str
    ):
        super().__init__(
            github_id=github_id,
            github_name=github_name,
            sender_id=sender_id
        )


class Repository(dict):
    def __init__(
            self,
            repository_url: str,
            repository_name: str,
            repository_id: str,
    ):
        super().__init__(
            repositoryId=repository_id,
            repositoryName=repository_name,
            repositoryUrl=repository_url
        )


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


class Webhook(dict):
    ID = '_id'
    SECRET = 'secret'
    CRATED_AT = 'createdAt'
    USER = 'user'
    REPOSITORY = 'repository'
    EVENT_AMT = 'evnetAmt'

    def __init__(
            self,
            id_: UUID,
            secret: str,
            user: WebhookUser,
            repository: Repository,
            created_at: datetime,
            event_amt: Optional[int] = 0,
    ):
        super().__init__(
            _id=str(id_),
            secret=secret,
            createdAt=created_at,
            user=user,
            eventAmt=event_amt,
            repository=repository
        )
