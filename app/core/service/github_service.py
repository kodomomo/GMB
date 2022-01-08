from abc import ABC, abstractmethod

from app.util.parser.github_parser import *
from app.util.parser.messenger_parser import *

from app.util.sql.dao.bot_dao import *
from app.util.sql.dao.repository_dao import *

from app.util.sql.entity.bot_entity import Bot
from app.util.sql.entity.repostiroy_entity import Repository


class GithubService(ABC):

    @abstractmethod
    async def execute_by_type(self, req: Request): pass


class GithubServiceImpl(GithubService):

    def __init__(self, git_parser: GitParser, bot_dao: BotDAO, repo_dao: RepositoryDAO):
        self.__git_parser = git_parser
        self.__bot_dao = bot_dao
        self.__repo_dao = repo_dao

    async def execute_by_type(self, req: Request):
        event_type = req.headers.get('X-GitHub-Event')
        body = await req.json()
        provide_type = {
            'ping': self.__type_is_ping,
            'push': self.__type_is_push,
            'issue': self.__type_is_issue,
            'pull_request': self.__type_is_pr
        }
        try:
            provide_type[event_type](body)
        except TypeError:
            return HTTPException(400, 'NONE PROVIDE TYPE')

    def __type_is_ping(self, bot_id: str, body: dict):
        repo_information = self.__git_parser.parse_ping(body)
        self.__bot_dao.update_repo_id(bot_id, repo_information['full_name'])

        new_repository = Repository(repo_information['full_name'], repo_information['is_public'])
        self.__repo_dao.insert_repository(new_repository)
        # TODO 웹훅 등록 성공 알림 발송

    def __type_is_push(self, bot_id: str, body: dict):
        parsed_push_body = self.__git_parser.parse_push(body)
        self.__change_variable_which_is_not_valid(bot_id, parsed_push_body)
        # TODO PUSH 알림 페메로 발송

    def __type_is_issue(self, bot_id: str, body: dict):
        parsed_issue_body = self.__git_parser.parse_issue(body)
        self.__change_variable_which_is_not_valid(bot_id, parsed_issue_body)
        # TODO ISSUE 알림 페메로 발송

    def __type_is_pr(self, bot_id: str, body: dict):
        parsed_pr_body = self.__git_parser.parse_pr(body)
        self.__change_variable_which_is_not_valid(bot_id, parsed_pr_body)
        # TODO PR 알림 페메로 발송

    def __change_variable_which_is_not_valid(self, bot_id: str, body: dict):
        repo_id = body['repository']['full_name']
        is_public = body['repository']['is_public']

        self.__check_repo_name__is_valid(repo_id, bot_id)
        self.__repo_dao.increase_1_about_event_amt(repo_id)
        self.__repo_dao.update_is_public(repo_id, is_public)

    def __check_repo_name__is_valid(self, repo_id: str, bot_id: str):
        if self.__bot_dao.select_repo_id(bot_id) != repo_id:
            self.__bot_dao.update_repo_id(bot_id, repo_id)
            self.__repo_dao.update_repo_id_and_url(repo_id)
