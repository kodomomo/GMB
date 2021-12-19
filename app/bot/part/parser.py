from abc import ABC, abstractmethod
from fastapi import HTTPException, Request


class Parser(ABC):

    @abstractmethod
    def parse(self, req: Request): pass


class ParserImpl(Parser):

    async def parse(self, req: Request):
        event_type = req.headers.get('X-GitHub-Event')
        body = await req.json()
        if self.__check_provide_type(event_type):
            return self.__execute_method_by_type(event_type, body)

    def __check_provide_type(self, type: str):
        provide_type = {
            'issues': True,
            'pull_request': True,
            'ping': True,
            'push': True
        }
        return type in provide_type

    def __execute_method_by_type(self, type: str, body: dict):
        provide_method_by_type = {
            'issues': self.__parse_issue,
            'pull_request': self.__parse_pr,
            'ping': self.__parse_ping,
            'push': self.__parse_push
        }
        return provide_method_by_type[type](body)

    def __parse_ping(self, body: dict):
        return self.__get_repo_name_url_private(body)

    def __parse_push(self, body: dict):
        return {
            'repository': self.__get_repo_name_url_private(body),
            'sender': body['sender']['login']
        }

    def __parse_issue(self, body: dict):
        return {
            'repository': self.__get_repo_name_url_private(body),
            'event_sender': body['sender']['login'],
            'issue_action': body['action'],
            'issue_title': body['title'],
            'issue_url': body['issue']['url'],
        }

    def __parse_pr(self, body: dict):
        return {
            'repository': self.__get_repo_name_url_private(body),
            'event_sender': body['sender']['login'],
            'pr_action': body['action'],
            'pr_title': body['title'],
            'pr_url': body['url']
        }

    @staticmethod
    def __get_repo_name_url_private(body: dict):
        repo_full_name = body['repository']['full_name']
        return {
            'private': body['repository']['private'],
            'full_name': repo_full_name,
            'url': 'github.com/' + repo_full_name
        }
