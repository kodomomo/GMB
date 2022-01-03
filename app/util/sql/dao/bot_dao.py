from abc import ABCMeta, abstractmethod

import pymysql
from config import DbConfig

from app.util.sql.entity.bot_entity import Bot

class BotDAO(ABCMeta): pass


class BotDAOImpl:

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
        created_at = bot.get_created_at()
        psid = bot.get_psid()
        repo_name = bot.get_repo_name()
        self.__cursor.execute(
            f'insert into bot(id,name,created_at,psid,repo_name) values(%s,%s,%s,%s,%s)'
            ,(id,name,created_at,psid,repo_name)
        )


if __name__ == '__main__':
    bot = Bot('sdf', 'qweqweqweqe')
    config =DbConfig()
    impl = BotDAOImpl(config)
    impl.insert_new_bot(bot)
