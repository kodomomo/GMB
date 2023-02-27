from uuid import uuid4

from app.config import BASE_URL
from app.core.messenger.api import MessagePayload
from app.util.parser.messenger import payload_to_message
from app.core.data.mongo.pending_webhook.command import create_pending_webhook
from app.core.data.request.messenger import send_message, PENDING_MESSAGE


def initialize_pending_hook(message: MessagePayload):
    id_ = uuid4()
    parsed_message = payload_to_message(message)

    create_pending_webhook(
        id_=id_,
        secret=parsed_message['secret'],
        sender_id=parsed_message['sender'],
    )

    send_message(
        message_text=PENDING_MESSAGE.format(
            base_url=BASE_URL,
            secret=parsed_message['secret'],
            id_=id_,
        ),
        recipient_id=parsed_message['sender']
    )
