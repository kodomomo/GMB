from abc import ABC, abstractmethod

from app.util.parser.github_parser import *
from app.util.parser.messenger_parser import *

from app.util.sql.dao.bot_dao import *
from app.util.sql.dao.repository_dao import *

from app.util.sql.entity.bot_entity import Bot
from app.util.sql.entity.repostiroy_entity import Repository


class GithubService(ABC):

    @abstractmethod
    async def execute_by_type(self, request: Request): pass


class GithubServiceImpl(GithubService):

    def __init__(self, git_parser: GitParser, bot_dao: BotDAO, repo_dao: RepositoryDAO):
        self.__git_parser = git_parser
        self.__bot_dao = bot_dao
        self.__repo_dao = repo_dao

    async def execute_by_type(self, request: Request):
        event_type = request.headers.get('X-GitHub-Event')
        body = await request.json()
        provide_type = {
            'ping': self.__notify_ping,
            'push': self.__count_push,
            'issue': self.__notify_issue,
            'pull_request': self.__notify_pr
        }
        try:
            return provide_type[event_type](body)
        except KeyError:
            raise HTTPException(400,'NONE PROVIDE TYPE')

    def __notify_ping(self): pass

    def __notify_issue(self): pass

    def __count_push(self): pass

    def __notify_pr(self): pass
