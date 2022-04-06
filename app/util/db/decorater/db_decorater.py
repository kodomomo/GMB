from ...db import get_session

from ...parser.github_parser import GithubParser

from ..model.repository import Repository


# 데코레이터마다 세션을 생성하는 것은 그릇된 행동이 아닐까?

def create_new_bot(func):
    def wrapper(bot_id: str, body: dict):

        session = get_session()
        repo_name = GithubParser.get_repository_name(body)

        try:
            session.add(Repository(repo_name['name']))
            session.commit()
        except:
            session.rollback()

        func(bot_id, body)

    return wrapper


def update_event_amount(func):
    def wrapper(bot_id: str, body: dict):
        session = get_session()
        parsed_issue = GithubParser.parse_issues(body)
        repo_name = parsed_issue['repo_name']

        try:
            pass
        except:
            pass

        func(bot_id, body)

    return wrapper
