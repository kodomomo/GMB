from jwt import encode
from time import time
from requests import post, get

from git_hub.config import PEM_CONTENT, GITHUB_APP_ID


def get_app_jwt():
    return encode(
        payload={
            'iat': int(time()),
            'exp': int(time()) + 600,
            'iss': GITHUB_APP_ID
        },
        key=PEM_CONTENT,
        algorithm='RS256'
    )


# url = f"https://api.github.com/app/installations/{GITHUB_APP_ID}/access_tokens"
url = 'https://api.github.com/app'
jwt_ = get_app_jwt()

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {jwt_}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = get(url=url, headers=headers)

from pprint import pprint

# pprint(response.json())

# https://api.github.com/app/installations/:installation_id/access_tokens

required_list = map(lambda x: {
    'url': x['access_tokens_url'],
    'permissions': x['permissions'],
    'user': x['account']['login']
}, get(
    headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {jwt_}"
    },
    url='https://api.github.com/app/installations'
).json()
                    )

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

pprint(
    post(
        url='https://api.github.com/repos/Kodomomo/GMB/hooks',
        headers={
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {user_list["kodomomo"]["token"]}',
            'X-GitHub-Api-Version': '2022-11-28'
        },
        json={
            "name": "web",
            "active": True,
            "events": [
                "ping",
                "push",
                "pull_request"
                ""
            ],
            "config": {
                "url": "https://ff8c-211-36-142-138.jp.ngrok.io/test",
                "content_type": "json"
            }
        }
    ).json()
)

if __name__ == '__main__':
    pass
