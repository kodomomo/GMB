from fastapi import FastAPI

from ..external_api.github_api import github_router

from ..external_api.messenger_api import messenger_router


def create_app():
    app = FastAPI()

    app.include_router(github_router)

    app.include_router(messenger_router)

    return app


app = create_app()
