from fastapi import FastAPI
from app.core.github.api import github_webhook_router


def include_github_router(app: FastAPI):
    app.include_router(github_webhook_router)
