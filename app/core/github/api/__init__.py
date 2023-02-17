from uuid import UUID

from fastapi import APIRouter, Request

from app.core.github.logic import check_webhook_valid

github_webhook_router = APIRouter(
    prefix='/github'
)


@github_webhook_router.post('/webhook/{bot_id}')
async def handle_webhook(bot_id: UUID, request: Request):
    await check_webhook_valid(bot_id, request)

    # PING, PUSH, PULL_REQUEST

    # ELSE
    