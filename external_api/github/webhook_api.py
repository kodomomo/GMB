from fastapi import APIRouter, Request

from app.core.service.github_service import *

github_router = APIRouter()


@github_router.post('/github/{bot_id}')
def get_webhook_from_github(request: Request):  pass
