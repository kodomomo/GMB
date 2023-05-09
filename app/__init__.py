from fastapi import FastAPI

from app.core.github import include_github_router
from app.core.gmb import include_gmb_router
from app.core.messenger import include_messenger_router


def create_app():
    app = FastAPI()

    # Router
    include_github_router(app)
    include_messenger_router(app)
    include_gmb_router(app)

    return app
