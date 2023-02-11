from fastapi import FastAPI

from app.core.facebook.api.webhook import messenger_router
from app.core.facebook.api.oauth import fb_oauth_router


def include_messenger_router(app: FastAPI):
    app.include_router(messenger_router)
    app.include_router(fb_oauth_router)