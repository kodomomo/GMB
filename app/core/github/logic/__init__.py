from uuid import UUID
from fastapi import Request

from app.common.exception.github import TypeNotJsonException
from app.common.security.github import check_security_set, check_security_correct
from app.core.data.mongo.query import get_pending_webhook


async def check_webhook_valid(bot_id: UUID, request: Request):
    pending = get_pending_webhook(bot_id)
    payload = await request.body()

    security_header = check_security_set(request.headers)
    check_security_correct(pending['secret'], security_header, payload)

    if request.headers.get('content-type') != 'application/json':
        raise TypeNotJsonException
