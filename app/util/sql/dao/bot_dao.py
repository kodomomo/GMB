from abc import ABCMeta, abstractmethod

import pymysql
from config import DbConfig

class BotDAO(ABCMeta): pass


class BotDAOImpl:

    def __init__(self):
        self.__DB = pymysql.connect(
            host=DbConfig.HOST,
            port=DbConfig.PORT,
            user=DbConfig.USER,
            password=DbConfig.PASSWORD,
            charset=DbConfig.CHARSET,
            database='kodomo_dragon',
            autocommit=True,
        )


    def insert_new_bot(self): pass

