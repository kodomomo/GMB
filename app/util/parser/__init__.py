from .github_parser import GithubParser

parsed_by_type = {
    'ping': GithubParser.get_repository_name,
    'push': GithubParser.get_repository_name,
    'issues': GithubParser.parse_issues,
    'pull_request': GithubParser.parse_pr
}