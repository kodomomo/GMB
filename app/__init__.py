from fastapi import FastAPI
from .api.endpoint import bot_router


def creat_app():
    app = FastAPI()

    app.include_router(bot_router)

    return app
