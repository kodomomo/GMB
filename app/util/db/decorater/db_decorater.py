from ...db import get_session

from ...parser.github_parser import GithubParser

from ..model.repository import Repository


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
