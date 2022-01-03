from abc import ABCMeta, abstractmethod

import pymysql
from config import DbConfig

from app.util.sql.entity.repostiroy_entity import Repository


class RepositoryDAO(ABCMeta): pass


class RepositoryDAOImpl:

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
