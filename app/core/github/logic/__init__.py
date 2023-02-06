from pprint import pprint

from requests import post

from app.core.github.logic.waiting import required_list
from app.security.github import get_app_jwt

user_list = {}
for obj in required_list:
    user_list[obj['user']] = post(
        url=obj['url'],
        headers={
            'Authorization': f'Bearer {get_app_jwt()}',
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
    ).json()

pprint(user_list)