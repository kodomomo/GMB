from uuid import UUID

from app.core.data.mongo.token.query import get_page_access_token
from app.core.data.mongo.webhook import Webhook, User
from app.core.data.mongo.webhook.command import update_amt
from app.core.data.mongo.webhook.query import get_webhook_by_id
from app.core.data.request.messenger import send_message
from app.util.parser.github.issue import parse_issue, get_type


async def handle_issue_event(bot_id: UUID, event_type: str, request: dict):
    if get_type(request) == 'opened':
        update_amt(bot_id, Webhook.Amt.ISSUE)
        webhook = get_webhook_by_id(bot_id)
        parsed_issue = parse_issue(request)

        message = parsed_issue['repository_name'] + r' Repository에서\n' \
                                                    rf'{parsed_issue["user"]}님이 [ {parsed_issue["title"]} ] Issue를 열었습니다.\n\n' \
                                                    rf'🔀 {parsed_issue["url"]}'

        send_message(
            get_page_access_token(),
            webhook[Webhook.USER][User.SENDER_ID],
            message
        )
