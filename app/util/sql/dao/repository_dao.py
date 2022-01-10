from abc import ABC, abstractmethod

import pymysql
from pymysql.cursors import DictCursor
from config import DbConfig

from app.util.sql.entity.repostiroy_entity import Repository


class RepositoryDAO(ABC):

    @abstractmethod
    def insert_repository(self, repository: Repository): pass

    @abstractmethod
    def update_is_public(self, repo_id: str, is_public: bool): pass

    @abstractmethod
    def increase_1_about_event_amt(self, repo_id: str): pass

    @abstractmethod
    def update_repo_id_and_url(self, repo_id: str): pass

    @abstractmethod
    def select_is_public(self, repo_id: str): pass


class RepositoryDAOImpl(RepositoryDAO):

    def __init__(self, config: DbConfig):
        self.__db = pymysql.connect(
            host=config.HOST,
            port=config.PORT,
            user=config.USER,
            password=config.PASSWORD,
            charset=config.CHARSET,
            database='kodomo_dragon',
            autocommit=True,
        )
        self.__cursor = self.__db.cursor(DictCursor)

    def insert_repository(self, repository: Repository):
        name = repository.get_name()
        url = repository.get_url()
        is_public = repository.get_is_public()
        self.__cursor.execute(
            f'insert into repository(id,url,is_public) values("{name}","{url}",{is_public});'
        )

    def update_is_public(self, is_public: bool, repo_id: str):
        self.__cursor.execute(
            f'update repository set is_public={is_public} where id="{repo_id}";'
        )

    def increase_1_about_event_amt(self, repo_id: str):
        self.__cursor.execute(
            f'update repository set event_amt=1 + event_amt where id="{repo_id}";'
        )

    def update_repo_id_and_url(self, repo_id: str):
        self.__cursor.execute(
            f'update repository'
            f' set id="{repo_id}, url="{"github.com/" + repo_id}"'
            f'" where id="{repo_id}";'
        )

    def select_is_public(self, repo_id: str):
        self.__cursor.execute(
            f'select is_public from repository where id="{repo_id}";'
        )
        is_public = self.__cursor.fetchone()
        return is_public
