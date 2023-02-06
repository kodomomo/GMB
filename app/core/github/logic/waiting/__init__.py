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
