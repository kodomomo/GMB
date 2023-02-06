from fastapi import APIRouter, Request

github_webhook_router = APIRouter(
    prefix='/github/webhook'
)


@github_webhook_router.post('/webhook')
async def handle_install_event(request: Request):
    from pprint import pprint

    pprint(await request.json())



@github_webhook_router.post('/webhook/{repo_id}')
def handle_repo_event(repo_id: str):
    pass
