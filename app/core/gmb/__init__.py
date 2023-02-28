from fastapi import FastAPI


def include_gmb_router(app: FastAPI):

    from app.core.gmb.api import gmb_router

    app.include_router(gmb_router)
