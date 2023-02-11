from fastapi import APIRouter

from app.core.data.request.facebook import STATE

from app.core.data.request.facebook import get_token, get_page_token

fb_oauth_router = APIRouter(
    prefix='/facebook'
)


@fb_oauth_router.get('/redirect')
def test_redirect(code: str, state: str):
    assert state == STATE

    token = get_token(code)['access_token']

    return get_page_token(token)
