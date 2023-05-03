from uuid import UUID

from app.core.data.mongo.webhook import User, Repository
from app.core.data.mongo.pending_webhook import PendingWebhook
from app.core.data.mongo.pending_webhook.query import get_pending_webhook_and_delete
from app.core.data.mongo.webhook.command import create_webhook
from app.util.request.messenger import send_message
from app.util.parser.github.ping import parse_ping_event


async def handle_ping_event(bot_id: UUID, event_type: str, request: dict):
    pending_webhook = get_pending_webhook_and_delete(bot_id)
    parsed_payload = parse_ping_event(request)

    create_webhook(
        id_=pending_webhook[PendingWebhook.ID],
        secret=pending_webhook[PendingWebhook.SECRET],
        user=User(
            sender_id=pending_webhook[PendingWebhook.SENDER_ID],
            github_id=parsed_payload['github_id'],
            github_name=parsed_payload['github_name']
        ),
        repository=Repository(
            repository_id=parsed_payload['repository_id'],
            repository_url=parsed_payload['repository_url'],
            repository_name=parsed_payload['repository_name']
        )
    )

    send_message(
        pending_webhook[PendingWebhook.SENDER_ID],
        parsed_payload['repository_name'] + ' Repository가 정상적으로 등록되었습니다!'
    )
