import os

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session


class __ORM_PART:
    __ENGINE = create_engine('mysql+pymysql://root:qwer1234@localhost:3306/gmb')  # mysql+pymysql://root:qwer1234@localhost:3306/gmb
    SESSION = scoped_session(sessionmaker(bind=__ENGINE, autocommit=False, autoflush=False))


def get_session(): return __ORM_PART.SESSION()


def close_session(session: __ORM_PART.SESSION): session.close()
