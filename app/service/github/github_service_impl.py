from ...util.parser.github_parser import GithubParser


class GithubServiceImpl:

    @staticmethod
    def when_ping(bot_id: str, body: dict) -> dict:
        print(bot_id)
        repo_name = GithubParser.get_repository_name(body)
        return repo_name

    @staticmethod
    def when_issue(bot_id: str, body: dict) -> dict:
        print(bot_id)
        return GithubParser.parse_issues(body)

    @staticmethod
    def when_pr(bot_id: str, body: dict) -> dict:
        print(bot_id)
        return GithubParser.parse_pr(body)
