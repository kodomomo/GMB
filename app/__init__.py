from fastapi import FastAPI
from app.main.endpoint.bot_endpoint import bot_router


def create_app():

    app = FastAPI()

    app.include_router(bot_router)

    return app
