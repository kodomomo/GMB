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
print(get_app_jwt())

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {jwt_}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = get(url=url, headers=headers)

from pprint import pprint
pprint(response.json())

if __name__ == '__main__':
    pass