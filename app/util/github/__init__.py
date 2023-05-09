from uuid import UUID
from fastapi import Request

from app.util.github.webhook import check_security_set, check_security_correct
# from app.core.data.mongo.pending_webhook.query import get_pending_secret
# from app.core.data.mongo.webhook.query import get_secret_by_id
from app.core.github.logic.event import EventType
from app.util.parser.github import get_event_type


async def check_webhook_valid(bot_id: UUID, request: Request):
    event_type = get_event_type(request)
    secret = get_pending_secret(bot_id) if event_type == EventType.PING else get_secret_by_id(bot_id)

    payload = await request.body()

    security_header = check_security_set(request.headers)
    # check_security_correct(secret, security_header, payload)

    if request.headers.get('content-type') != 'application/json':
        raise # TODO
