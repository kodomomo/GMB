from fastapi import APIRouter


def create_api_router(base_url: str):
    return APIRouter(
        prefix='/'+base_url
    )
