from fastapi import APIRouter, Request

github_router = APIRouter(
    prefix='/github'
)


@github_router.post('/webhook')
def handle_install_event():
    pass


@github_router.post('/webhook/{repo_id}')
def handle_repo_event(repo_id: str):
    pass
