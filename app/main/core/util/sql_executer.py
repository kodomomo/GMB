from config import Config
from abc import ABC  # abstractmethod
import pymysql
from pymysql.cursors import DictCursor


class SqlExecuter(ABC): pass


class SqlExecuterImpl(SqlExecuter):

    @staticmethod
    def __get_db_and_cursor():
        config = Config
        __db = pymysql.connect(
            host=config.HOST,
            port=config.PORT,
            charset=config.CHARSET,
            user=config.USER,
            password=config.PASSWORD
        )
        __cursor = __db.cursor(DictCursor)
        return {
            'db': __db,
            'cursor': __cursor
        }