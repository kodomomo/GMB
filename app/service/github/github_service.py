from ...util.parser.github_parser import GithubParser

from ...util.db.model.repository import Repository

from ...util.db import get_session


class GithubService:

    @staticmethod
    def when_ping(bot_id: str, body: dict) -> dict:
        session = get_session()
        repo_name = GithubParser.get_repository_name(body)

        try:
            session.add(Repository(repo_name['name']))
            session.commit()
        except:
            print('rollback\n\n\n\n\n\n')
            session.rollback()

        return body

    @staticmethod
    def when_issue(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_issues(body)

    @staticmethod
    def when_pr(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_pr(body)
