from .github_service import GithubService

act_service_by_type = {
    'ping': GithubService.when_ping,
    'push': GithubService.when_push,
    'issues': GithubService.when_issue,
    'pull_request': GithubService.when_pr
}

