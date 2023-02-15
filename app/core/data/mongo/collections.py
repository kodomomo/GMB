from uuid import UUID
from typing import Optional, List
from datetime import datetime

from app.util.time import utc_now, ktc_now


class CollectionNames:
    TOKEN = 'messengerToken'
    WEBHOOK_USER = 'webhookUser'
    PENDING_WEBHOOK = 'pendingWebhook'
    WEBHOOK = 'webhook'
    REPOSITORY = 'repository'

    NAME_LIST = [TOKEN, WEBHOOK, PENDING_WEBHOOK, WEBHOOK_USER, REPOSITORY]


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
    RECEIPT_ID = 'receiptId'

    def __init__(
            self,
            github_id: str,
            github_name: str,
            receipt_id: str
    ):
        super().__init__(
            github_id=github_id,
            github_name=github_name,
            receipt_id=receipt_id
        )


class PendingWebhook(dict):
    ID = '_id'
    SECRET = 'secret'
    SENDER_ID = 'senderId'
    RECEIPT_ID = 'receiptId'
    CREATED_AT = 'createdAt'

    def __init__(self, id_: UUID, secret: str, sender_id: str, receipt_id: str, created_at: Optional[datetime] = utc_now()):
        super().__init__(
            _id=str(id_),
            secret=secret,
            senderId=sender_id,
            receiptId=receipt_id,
            createdAt=created_at
        )


class Webhook(dict):
    ID = '_id'
    SECRET = 'secret'
    CRATED_AT = 'createdAt'
    USER = 'user'
    EVENT_AMT = 'evnetAmt'

    def __init__(
            self,
            id_: UUID,
            secret: str,
            user: WebhookUser,
            created_at: Optional[datetime] = ktc_now(),
            event_amt: Optional[int] = 0,
    ):
        super().__init__(
            _id=str(id_),
            secret=secret,
            createdAt=created_at,
            user=user,
            eventAmt=event_amt
        )


class Repository(dict):
    ID = '_id'
    FULL_NAME = 'fullName'
    DIRECT_URL = 'directUrl'
    user = 'user'

    def __init__(
            self,
            id_: UUID,
            full_name: str,
            direct_url: str,
            hook_user: List[WebhookUser]
    ):
        super().__init__(
            _id=str(id_),
            fullName=full_name,
            directUrl=direct_url,
            user=hook_user
        )
