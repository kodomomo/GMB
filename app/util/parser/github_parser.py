from abc import ABC, abstractmethod
from fastapi import HTTPException, Request


class GitParser(ABC):

    @abstractmethod
    def parse_ping(self, body: dict): pass

    @abstractmethod
    def parse_push(self, body: dict): pass

    @abstractmethod
    def parse_issue(self, body: dict): pass

    @abstractmethod
    def parse_pr(self,body: dict): pass


class GitParserImpl(GitParser):

    def parse_ping(self, body: dict):
        return self.__get_repo_name_url_private(body)

    def parse_push(self, body: dict):
        return {
            'repository': self.__get_repo_name_url_private(body),
            'sender': body['sender']['login']
        }

    def parse_issue(self, body: dict):
        return {
            'repository': self.__get_repo_name_url_private(body),
            'event_sender': body['sender']['login'],
            'issue_action': body['action'],
            'issue_title': body['title'],
            'issue_url': body['issue']['url'],
        }

    def parse_pr(self, body: dict):
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
            'is_public': body['repository']['private'],
            'full_name': repo_full_name,
            'url': 'github.com/' + repo_full_name
        }
