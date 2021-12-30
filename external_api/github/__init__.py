from fastapi import APIRouter,Request

github_router = APIRouter()

@github_router.post('/{bot_id}')
def get_webhook_from_github(request:Request): pass
    #core의 서비스 딴으로 넘기면 됨.
    #서비스는 request만 받으면 됨, 누가 주는 지 알 필요도 없고 알아도 안 됨.

