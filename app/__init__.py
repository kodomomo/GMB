from fastapi import FastAPI

from app.core.data.mongo import init_mongo
from app.core.github import include_github_router
from app.core.gmb import include_gmb_router
from app.core.messenger import include_messenger_router


def create_app():
    app = FastAPI()

    # Mongo
    init_mongo()

    # Router
    include_github_router(app)
    include_messenger_router(app)
    include_gmb_router(app)

    return app

# TODO
# 1. Model Class에서 @Property 변수로 접근 가능하게 해주기
# 2. query에서 find 함수들 return 값 Decorator를 통해서 Model로 바꿔주기