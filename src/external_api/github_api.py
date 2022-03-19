from fastapi import Request, APIRouter

github_router = APIRouter(
    prefix='/github'
)


@github_router.post('/{bot_id}')
def aa(request: Request):

    print(request)

