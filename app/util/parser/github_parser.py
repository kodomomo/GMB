from abc import ABC, abstractmethod

from fastapi import HTTPException, Request


class GitParser(ABC):

    @abstractmethod
    def parse(self, event_type: str, body: dict) -> dict: pass


class GitParserImpl(GitParser):

    def parse(self, event_type: str, body: dict):
        operate_parse_type = {
            'issue': self.__parse_issue,
            'pull_request': self.__parse_pr
        }
        try:
            return operate_parse_type[event_type](body)
        except KeyError:
            return {
                'repository' : self.__parse_about_repository(body)
            }

    @staticmethod
    def __parse_about_repository(body: dict):
        repo_full_name = body['repository']['full_name']
        return {
            'name': repo_full_name,
            'url': 'github.com/' + repo_full_name,
            'private': body['repository']['private'],
        }

    def __parse_issue(self, body: dict):
        return {
            'sender': body['sender']['login'],
            'repository': self.__parse_about_repository(body),
            'issue': {
                'action': body['action'],
                'title': body['issue']['title'],
                'url': body['issue']['html_url'],
            }
        }

    def __parse_pr(self, body: dict):
        return {
            'sender': body['sender']['login'],
            'repository': self.__parse_about_repository(body),
            'pr': {
                'action': body['action'],
                'title': body['title'],
                'url': body['html_url']
            }
        }