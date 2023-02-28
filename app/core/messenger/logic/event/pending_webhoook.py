from uuid import uuid4

from app.config import BASE_URL
from app.util.parser.messenger import Message
from app.core.data.mongo.pending_webhook.command import create_pending_webhook
from app.core.data.request.messenger import send_message, PENDING_MESSAGE


def initialize_pending_hook(message: Message):
    id_ = uuid4()

    create_pending_webhook(
        id_=id_,
        secret=message.content,
        sender_id=message.sender,
    )

    send_message(
        message_text=PENDING_MESSAGE.format(
            base_url=BASE_URL,
            secret=message.content,
            id_=id_,
        ),
        recipient_id=message.sender
    )
