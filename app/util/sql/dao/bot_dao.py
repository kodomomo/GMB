import pymysql
from pymysql.cursors import DictCursor
from config import DbConfig

from app.util.sql.entity.bot import Bot


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
        self.__cursor = self.__db.cursor(DictCursor)

    def new_bot(self, bot: Bot):
        self.__cursor.execute(
            'insert into bot '
            'values('
            f'"{bot.get_name()}"'
            f'"{bot.get_repository().get_name()}"'
            f'"{bot.get_psid()}"'
        )
