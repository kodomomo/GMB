from uuid import UUID

from app.core.data.mongo.webhook import Webhook, User, Repository
from app.core.data.mongo.webhook.query import get_webhook_by_id
from app.util.request.messenger import send_message


async def handle_none_provide_event(bot_id: UUID, event_type: str, request: dict):
    webhook = get_webhook_by_id(bot_id)

    message = webhook[Webhook.REPOSITORY][Repository.NAME] + rf' Repository에서 {event_type} Event가 발생하였습니다.\n\n' \
                                                             rf'✅ {webhook[Webhook.REPOSITORY][Repository.URL]}'

    send_message(
        webhook[Webhook.USER][User.SENDER_ID],
        message
    )
