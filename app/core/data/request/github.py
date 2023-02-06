from typing import Optional
from requests import post, get


def get_header(jwt_token: str):
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def github_get(url: str, token: str):
    return get(
        url=url,
        headers=get_header(token)
    )


def github_post(url: str, token: str, body: Optional[dict] = None):
    return post(
        url=url,
        headers=get_header(token),
        json=body
    )
