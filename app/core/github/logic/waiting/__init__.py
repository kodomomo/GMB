from requests import get

from app.core.data.request.github import github_get
from app.security.github import get_app_jwt

required_list = map(lambda x: {
    'url': x['access_tokens_url'],
    'permissions': x['permissions'],
    'user': x['account']['login']
}, github_get(
    url='https://api.github.com/app/installations',
    token=get_app_jwt()
    ).json()
)


url = 'https://api.github.com/app'
jwt_ = get_app_jwt()

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {jwt_}",
    "X-GitHub-Api-Version": "2022-11-28"
}

response = get(url=url, headers=headers)