from ...service.github import act_service_by_type

from fastapi import APIRouter, Request, status, HTTPException

github_router = APIRouter(
    prefix='/github'
)


@github_router.post('/{bot_id}')
async def get_webhook_by_each_bot(bot_id: str, request: Request):
    try:
        type = request.headers.get('X-GitHub-Event')
        body = await request.json()

        return act_service_by_type[type](bot_id, type, body)

    except KeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="None Provide Type")
