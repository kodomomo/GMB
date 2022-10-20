from fastapi import FastAPI

from app.core.github import github_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(github_router)

    return app
