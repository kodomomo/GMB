from fastapi import FastAPI

from app.core.data.mongo import init_mongo
from app.core.github import include_github_router
from app.core.facebook import include_messenger_router


def create_app():
    app = FastAPI()

    # Mongo
    init_mongo()

    # Router
    include_github_router(app)
    include_messenger_router(app)

    return app
