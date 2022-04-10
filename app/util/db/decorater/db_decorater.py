from ...db import get_session

from ...parser import parsed_by_type

from ..model.user import User
from ..model.repository import Repository


def create_bot(func):
    session = get_session()

    def wrapper(bot_id: str, type: str, body: dict):
        name = parsed_by_type[type](body)['repo_name']
        new_repo = Repository(name)
        try:
            session.add(new_repo)
            session.commit()
        except:
            session.rollback()
        return func(bot_id, type, body)

    return wrapper


def assign_bot(func):
    session = get_session()

    def wrapper(bot_id: str, type: str, body: dict):
        name = parsed_by_type[type](body)['repo_name']
        try:
            session.query(User).filter(User.bot_id == bot_id).update(
                {'repo_name': name}
            )
            session.commit()

        except: session.rollback()

        return func(bot_id, type, body)

    return wrapper


def increase_event_amount(func):
    session = get_session()

    def wrapper(bot_id: str, type: str, body: dict):
        name = parsed_by_type[type](body)['repo_name']
        try:
            session.query(Repository).filter(Repository.repo_name==name).update(
                {'event_amt': Repository.event_amt + 1}
            )
            session.commit()

        except: session.rollback()

        return func(bot_id, type, body)

    return wrapper
# send_messenger(func):
