from uuid import uuid4

from app.core.data.mongo.pending_webhook.command import create_pending_webhook
from app.core.data.mongo.token.query import get_page_access_token
from app.core.messenger.api import MessagePayload
from app.util.parser.messenger import payload_to_message
from app.core.data.request.messenger import send_message, PENDING_MESSAGE


def initialize_pending_hook(message: MessagePayload):
    id_ = uuid4()
    parsed_message = payload_to_message(message)
    page_access_token = get_page_access_token()

    create_pending_webhook(
        id_=id_,
        secret=parsed_message['secret'],
        sender_id=parsed_message['sender'],
    )

    send_message(
        page_access_token=page_access_token,
        message_text=PENDING_MESSAGE.format(
            webhook_id=id_,
            secret=parsed_message['secret']
        ),
        recipient_id=parsed_message['sender']
    )
