from fastapi import FastAPI

from app.core.messenger.api import messenger_router


def include_messenger_router(app: FastAPI):
    app.include_router(messenger_router)
