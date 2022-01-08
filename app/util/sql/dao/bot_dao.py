from abc import ABCMeta, abstractmethod

import pymysql
from config import DbConfig

from app.util.sql.entity.bot_entity import Bot


class BotDAO(ABCMeta):

    def insert_new_bot(cls, bot: Bot): pass

    def update_repo_id_in_bot(cls, bot_id: str, repo_id: str): pass


class BotDAOImpl(BotDAO):

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
        self.__cursor = self.__db.cursor()

    def insert_new_bot(self, bot: Bot):
        id = bot.get_bot_id()
        name = bot.get_bot_name()
        psid = bot.get_psid()
        repo_name = bot.get_repo_name()
        self.__cursor.execute(
            f'insert into bot(id,name,psid,repo_id) values(unhex(%s),%s,%s,%s)', (id, name, psid, repo_name)
        )

    def update_repo_id_in_bot(self, bot_id: str, repo_id: str):
        self.__cursor.execute(
            f'update bot set repo_id = "{repo_id}" where hex(id)="{bot_id}";'
        )

