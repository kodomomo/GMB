from fastapi import FastAPI
from app.core.github.api.webhook import github_webhook_router
from app.core.github.api.oauth import github_oauth_router


def include_github_router(app: FastAPI):
    app.include_router(github_webhook_router)
    app.include_router(github_webhook_router)
