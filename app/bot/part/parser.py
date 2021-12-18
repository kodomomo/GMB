from abc import ABC, abstractmethod
from fastapi import HTTPException, Request


class ParserImpl:

    def parse(self, req: Request):
        event_type = req.headers.get('X-GitHub-Event')
        if self.__check_type_is_one_of_provide(event_type):
            return self.__execute_method_by_type(event_type,req)

    def __check_type_is_one_of_provide(self, type: str):
        provide_type = {
            'issues': '',
            'pull_request': '',
            'ping': '',
            'push': ''
        }
        return provide_type.get(type) is not None

    def __execute_method_by_type(self, type: str, req: Request):
        provide_method_by_type = {
            'issues': self.__parse_issue,
            'pull_request': self.__parser_pr,
            'ping': self.__parser_ping,
            'push': self.__parser_push
        }
        return provide_method_by_type[type](req)

    def __parse_issue(self, req: Request): pass

    def __parser_pr(self, req: Request): pass

    def __parser_ping(self, req: Request): pass

    def __parser_push(self, req:Request): pass
