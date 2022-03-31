from .github_service import GithubService

act_service_by_type = {
    'ping': GithubService.when_ping,
    'issues': GithubService.when_issue,
    'pull_requests': GithubService.when_pr
}

