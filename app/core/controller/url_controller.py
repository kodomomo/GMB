from fastapi import APIRouter

url_router = APIRouter()


@url_router.get('/{bot_id}')
def show_each_bot_and_repository(): pass

