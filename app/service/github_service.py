from abc import ABC, abstractmethod

from app.util.parser.github_parser import *
from app.util.parser.messenger_parser import *

from app.util.sql.dao.bot_dao import *
from app.util.sql.dao.repository_dao import *


class GithubServiceImpl:

    def __init__(self, git_parser: GitParser, bot_dao: BotDAOImpl, repo_dao: RepositoryDAOImpl):
        self.__git_parser = git_parser
        self.__bot_dao = bot_dao
        self.__repo_dao = repo_dao

    def execute(self, request: Request):
        parsed_request = self.__parse_event(request)
        self.check_differences(parsed_request['repository']['name'])
        self.__repo_dao.increase_event_amt(parsed_request['repository']['name'])
        if parsed_request.get('sender') is not None: self.send_fm()

    async def __parse_event(self, request: Request) -> dict:
        event_type = request.headers.get('X-GitHub-Event')
        return self.__git_parser.parse(event_type, await request.json())

    def check_differences(self,repository_name: str):
        if self.__repo_dao.find_repository_by_name(repository_name) is None: raise HTTPException(400,'NONE REGISTERED REPOSITORY')
        pass

    def send_fm(self):
        notify_event_type = {
            'issue': True,
            'pull_request': True
        }
