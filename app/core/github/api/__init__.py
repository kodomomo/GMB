from uuid import UUID

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app.core.github.logic import act_by_event_type
from app.common.security.github import check_webhook_valid


github_webhook_router = APIRouter(
    prefix='/github'
)


@github_webhook_router.get('/webhook/{bot_id}')
async def redirect_to_how_to_use(bot_id: UUID, request: Request):
    return RedirectResponse('https://github.com/kodomomo/GMB/blob/master/README.md')


@github_webhook_router.post('/webhook/{bot_id}')
async def handle_webhook(bot_id: UUID, request: Request):

    await check_webhook_valid(bot_id, request)
    await act_by_event_type(bot_id, request)

