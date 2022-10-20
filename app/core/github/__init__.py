from fastapi import APIRouter

from app.core.github.service.handle_event import handle_event
from app.core.github.service.operator import github_service_operator

github_router = APIRouter()


@github_router.get('/test')
def get_request_by_yml():

    handle_event(github_service_operator['handle'])
