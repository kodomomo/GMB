from fastapi import APIRouter
from fastapi.responses import RedirectResponse

gmb_router = APIRouter()


@gmb_router.get('/')
def redirect_base():

    # TODO

    return RedirectResponse(
        url='https://www.youtube.com/watch?v=DDYJysAYVWo&t=0s'
    )
