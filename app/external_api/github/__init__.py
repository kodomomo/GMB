from ...service.github import act_service_by_type

from fastapi import APIRouter, Request

github_router = APIRouter(
    prefix='/github'
)


@github_router.post('/{bot_id}')
async def get_webhook_by_each_bot(bot_id: str, request: Request) -> Request:
    type = request.headers.get('X-GitHub-Event')
    body = await request.json()

    print(bot_id)
    print(type)

    return act_service_by_type[type](bot_id, body)
