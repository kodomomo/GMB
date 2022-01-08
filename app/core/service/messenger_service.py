from abc import ABC, abstractmethod

from app.util.parser.github_parser import *
from app.util.parser.messenger_parser import *

from app.util.sql.dao.bot_dao import *
from app.util.sql.dao.repository_dao import *

from app.util.sql.entity.bot_entity import Bot
from app.util.sql.entity.repostiroy_entity import Repository


class MessengerService(ABC): pass


class MessengerServiceImpl(MessengerService):

    def __init__(self, git_parser: GitParser, bot_dao: BotDAO, repo_dao: RepositoryDAO):
        self.__git_parser = git_parser
        self.__bot_dao = bot_dao
        self.__repo_dao = repo_dao

    def create_bot(self, name: str, psid: str):
        new_bot = Bot(name, psid)
        self.__bot_dao.insert_new_bot(new_bot)
