from fastapi import FastAPI
from external_api.github import github_router


def create_app():
    app = FastAPI()

    app.include_router(github_router)

    return app
