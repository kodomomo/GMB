from uuid import uuid4

from app.core.data.mongo.command import create_pending_webhook
from app.core.data.mongo.query import get_page_access_token
from app.core.messenger.api import MessagePayload
from app.util.parser.messenger import payload_to_message
from app.core.data.request.messenger import send_message, PENDING_MESSAGE


def initialize_pending_hook(message: MessagePayload):
    parsed_message = payload_to_message(message)
    page_access_token = get_page_access_token()

    create_pending_webhook(
        secret=parsed_message['secret'],
        sender_id=parsed_message['sender'],
        receipt_id=parsed_message['receipt']
    )

    send_message(
        page_access_token=page_access_token,
        message_text=PENDING_MESSAGE.format(
            webhook_id=uuid4(),
            secret=parsed_message['secret']
        ),
        recipient_id=parsed_message['sender']
    )
