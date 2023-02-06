from jwt import encode
from time import time

from app.config.github import GITHUB_APP_ID, PEM_CONTENT, ALGORITHM


def get_app_jwt():
    return encode(
        payload={
            'iat': int(time()),
            'exp': int(time()) + 600,
            'iss': GITHUB_APP_ID
        },
        key=PEM_CONTENT,
        algorithm=ALGORITHM
    )
