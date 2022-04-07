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

        return func(bot_id, body)

    return wrapper


def update_event_amount(func):
    session = get_session()

    def wrapper(bot_id: str, body: dict):
        parsed_issue = GithubParser.parse_issues(body)
        repo_name = parsed_issue['repo_name']

        try:
            session.query(Repository).filter(Repository.repo_name == repo_name).update({'event_amt': Repository.event_amt + 1})
            session.commit()
        except:
            session.rollback()

        return func(bot_id, parsed_issue)

    return wrapper
