from app.core.data.request.github import github_post


def create_webhook(token: str, owner: str, repository: str):
    github_post(
        url=f'https://api.github.com/repos/{owner}/{repository}/hooks',
        token=token,
        body={
            "name": "web",
            "active": True,
            "events": [
                "ping",
                "push",
                "pull_request"
            ],
            "config": {
                "url": "https://ff8c-211-36-142-138.jp.ngrok.io/test",
                "content_type": "json",
                "insecure_ssl": "0"
            }
        }
    )
