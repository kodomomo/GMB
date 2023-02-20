from uuid import UUID

from app.core.data.mongo.token.query import get_page_access_token
from app.core.data.mongo.webhook import Webhook, Repository, User
from app.core.data.mongo.webhook.command import update_amt
from app.core.data.mongo.webhook.query import get_webhook_by_id
from app.core.data.request.messenger import send_message
from app.util.parser.github.push import parse_push


async def handle_push_event(bot_id: UUID, event_type: str, request: dict):
    update_amt(bot_id, Webhook.Amt.PUSH)
    webhook = get_webhook_by_id(bot_id)
    parsed_push = parse_push(request)

    send_message(
        get_page_access_token(),
        webhook[Webhook.USER][User.SENDER_ID],
        parsed_push['name'] + rf' Repository에서 {parsed_push["commit_amt"]}개의 커밋이 Push 되었습니다.\n\n'
                                                       rf'📩 {parsed_push["url"]}'
    )
