from abc import ABC, abstractmethod

from app.util.parser.github_parser import *
from app.util.parser.messenger_parser import *

from app.util.sql.dao.bot_dao import *
from app.util.sql.dao.repository_dao import *

from app.util.sql.entity.bot_entity import Bot
from app.util.sql.entity.repostiroy_entity import Repository


class UrlService(ABC):
    pass


class UrlServiceImpl(UrlService): pass
