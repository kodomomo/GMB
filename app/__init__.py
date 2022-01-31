from fastapi import FastAPI
from external_api.github_api import github_router
from core.controller.url_controller import url_router

def create_app():

    app = FastAPI()

    app.include_router(github_router)
    app.include_router(url_router)

    return app
