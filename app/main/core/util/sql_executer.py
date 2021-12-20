from abc import ABC, abstractmethod

HOST = 'localhost'
USER = 'root'
PASSWORD = 'qwer1234'
PORT = 3306
CHARSET = 'utf8'


class SqlExecuter(ABC):
    pass


class SqlExecuterImpl(SqlExecuter):
    def __init__(self):
        import pymysql
        self.db = pymysql.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, charset=CHARSET)
        self.cursor = self.db.cursor()

