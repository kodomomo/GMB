from ...db import get_session

from ...parser import parsed_by_type

from ..model.repository import Repository


# 데코레이터마다 세션을 생성하는 것은 그릇된 행동이 아닐까?

def create_new_bot(func):
    def wrapper(bot_id: str, type: str, body: dict):
        session = get_session()
        repo_name = parsed_by_type[type](body)

        try:
            session.add(Repository(repo_name['name']))
            session.commit()
        except:
            session.rollback()

        return func(bot_id, type, repo_name)

    return wrapper


def update_event_amount(func):
    session = get_session()

    def wrapper(bot_id: str, type: str, body: dict):
        parsed_body = parsed_by_type[type](body)
        repo_name = parsed_body['repo_name']

        try:
            session.query(Repository).filter(Repository.repo_name == repo_name).update(
                {'event_amt': Repository.event_amt + 1}
            )
            session.commit()
        except:
            session.rollback()

        return func(bot_id, type, parsed_body)

    return wrapper

# notice_by_messenger

# add_repository_to_each_user
