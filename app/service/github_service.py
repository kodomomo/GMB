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
        parsed_request = self.__parse_request(request)
        repository = parsed_request['repository']['name']

        self.__check_repository_is_valid(repository)

        self.__apply_repository_changes(repository)

        if parsed_request['should_notify']: self.__notify_by_messenger()

    async def __parse_request(self, request: Request):
        event_type = request.headers.get('X-GitHub-Event')
        body = await request.json()
        return self.__git_parser.parse(event_type, body)

    def __check_repository_is_valid(self, name: str):
        if self.__repo_dao.find_repository_by_name(name) is None:
            raise HTTPException(400, 'CHECK REPOSITORY HAS REGISTER TO BOT')
            # 나중에 페메를 통해 URL에서 수정할 수 있도록 알려줘야 함

    def __apply_repository_changes(self, name: str):
        self.__repo_dao.increase_event_amt(name)

    def __notify_by_messenger(self):
        pass
