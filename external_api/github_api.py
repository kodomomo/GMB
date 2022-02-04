from fastapi import APIRouter, Request

github_router = APIRouter()


@github_router.post('/{bot_id}')
def get_webhook_from_github(request: Request):