from uuid import UUID

from app.core.data.mongo.token.query import get_page_access_token
from app.core.data.mongo.webhook import Webhook, User
from app.core.data.mongo.webhook.command import update_amt
from app.core.data.mongo.webhook.query import get_webhook_by_id
from app.core.data.request.messenger import send_message
from app.util.parser.github.pull_request import get_action, parse_pull_request


async def handle_pull_request_event(bot_id: UUID, event_type: str, request: dict):
    if get_action(request) == 'opened':
        update_amt(bot_id, Webhook.Amt.PULL_REQUEST)
        webhook = get_webhook_by_id(bot_id)
        parsed_pr = parse_pull_request(request)

        message = parsed_pr['repository'] + r' Repository에서\n' \
                                                 rf'{parsed_pr["user"]}님이 [ {parsed_pr["title"]} ] PR을 열었습니다\n\n' \
                                                 rf'🔥 {parsed_pr["url"]}'

        send_message(
            get_page_access_token(),
            webhook[Webhook.USER][User.SENDER_ID],
            message
        )
        print(message)