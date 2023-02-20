from uuid import UUID
from fastapi import Request

from app.core.data.mongo.collections import Webhook, WebhookUser, Repository
from app.core.data.mongo.token.query import get_page_access_token
from app.core.data.mongo.webhook.query import get_webhook_by_id
from app.core.data.request.messenger import send_message


async def handle_none_provide_event(bot_id: UUID, event_type: str, request: dict):
    webhook = get_webhook_by_id(bot_id)

    message = webhook[Webhook.REPOSITORY][Repository.NAME] + rf' Repository에서 {event_type} Event가 발생하였습니다.\n\n' \
                                                             rf'✅ 바로가기 \n    · {webhook[Webhook.REPOSITORY][Repository.URL]}'

    send_message(
        get_page_access_token(),
        webhook[Webhook.USER][WebhookUser.SENDER_ID],
        message
    )
