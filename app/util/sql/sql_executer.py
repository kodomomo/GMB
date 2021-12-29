from abc import ABC, abstractmethod

import pymysql
from pymysql.cursors import DictCursor

from config import DbConfig
from sql_executer_dao import *


class SqlExecuter(ABC):

    @abstractmethod
    def show_bot_and_relation_repository(self, bot_id: str): pass

    @abstractmethod
    def create_bot(self, create_bot_dao: CreateBotDAO): pass

    @abstractmethod
    def create_repository(self, create_repository_dao: CreateRepositoryDAO): pass

    @abstractmethod
    def update_repository_name_in_bot(self, update_repository_name_in_bot_dao: UpdateRepositoryNameInBotDAO): pass

    @abstractmethod
    def update_repo_event_amt(self, update_event_amt: UpdateEventAmountDAO): pass


class SqlExecuterImpl(SqlExecuter):

    def __init__(self, config: DbConfig):
        self.__db = pymysql.connect(
            host=config.HOST,
            port=config.PORT,
            charset=config.CHARSET,
            database='kodomo_dragon',
            autocommit=True,
            user=config.USER,
            password=config.PASSWORD
        )
        self.__cursor = self.__db.cursor(DictCursor)

    def show_bot_and_relation_repository(self, bot_id: str):
        bot = self.__select_all_from_bot(bot_id)
        return {
            'bot' : bot,
            'repository' : self.__find_repository_by_id(bot['repo_name'])
        }

    def create_bot(self, creat_bot_dao: CreateBotDAO):
        bot_setting = creat_bot_dao.get_field_variable_as_dict()
        bot_uuid = "UNHEX(REPLACE(UUID(),'-',''))"
        self.__cursor.execute(
            f'insert into bot(id,name,created_at,psid,repo_name) '
            f'values({bot_uuid},"{bot_setting["name"]}",now(),"{bot_setting["psid"]}","{bot_setting["repository_name"]}");'
        )
        self.__db.commit()

    def create_repository(self, create_repository_dao: CreateRepositoryDAO):
        repository_setting = create_repository_dao.get_field_variable_as_dict()
        self.__cursor.execute(
            f'insert into repository(name,url,is_public,event_amt) '
            f'values("{repository_setting["name"]}","{repository_setting["url"]}",{repository_setting["is_public"]},{repository_setting["event_amt"]}) '
        )
        self.__db.commit()

    def update_repository_name_in_bot(self, update_repository_name_in_bot_dao: UpdateRepositoryNameInBotDAO):
        repository_name = update_repository_name_in_bot_dao.get_field_variable_as_dict()['repository_name']
        bot_id = update_repository_name_in_bot_dao.get_field_variable_as_dict()['bot_id']
        self.__cursor.execute(
            f'update bot set repo_name="{repository_name}" where hex(id)="{bot_id}";'
        )
        self.__db.commit()

    def update_repo_event_amt(self, update_event_amt: UpdateEventAmountDAO):
        repo_name = update_event_amt.get_field_variable_as_dict()['repo_name']
        event_amt = update_event_amt.get_field_variable_as_dict()['event_amt']
        self.__cursor.execute(
            f'update repository set event_amt={event_amt} where name="{repo_name}"'
        )
        self.__db.commit()

    def __select_all_from_bot(self,bot_id: str):
        self.__cursor.execute(
            f'select hex(id),name,created_at,psid,repo_name from bot where hex(id)="{bot_id}";'
        )
        return self.__cursor.fetchone()

    def __find_repository_by_id(self,repo_name: str):
        self.__cursor.execute(
            f'select * from repository where name="{repo_name}"'
        )
        return self.__cursor.fetchone()


