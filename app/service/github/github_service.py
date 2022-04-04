from ...util.parser.github_parser import GithubParser


class GithubService:

    @staticmethod
    def when_ping(bot_id: str, body: dict) -> dict:
        repo_name = GithubParser.get_repository_name(body)
        return repo_name

    @staticmethod
    def when_issue(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_issues(body)

    @staticmethod
    def when_pr(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_pr(body)
