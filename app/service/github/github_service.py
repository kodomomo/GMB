from ...util.parser.github_parser import GithubParser

from ...util.db.model.repository import Repository

from ...util.db import get_session

from ...util.db.decorater.db_decorater import create_new_bot


class GithubService:

    """
        TODO
        이중 데코레이터의 동작 순서 알아보기
    """

    @staticmethod
    @create_new_bot
    def when_ping(bot_id: str, body: dict) -> dict:

        """
            TODO
            bot_id를 통해서 user 테이블에 repository 추가해줌.
            bot_id로 찾아낸 user 튜플들에 페메를 발송함.
        """

        return body

    @staticmethod
    def when_issue(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_issues(body)

    @staticmethod
    def when_pr(bot_id: str, body: dict) -> dict:
        return GithubParser.parse_pr(body)
