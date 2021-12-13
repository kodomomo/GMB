from abc import ABCMeta, abstractmethod
from fastapi import Request
from .payload.response import *

class Hatchling(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def get_data_from_request(self, req): pass

    @abstractmethod
    def __change_tier(self): pass

    @abstractmethod
    def return_bot_data(self): pass


class HatchlingImpl(Hatchling):

    repo_name: str
    repo_url: str

    def __init__(self, name: str):
        self.name = name
        self.tier = 'C'

    async def set_bot_repo(self,req:Request):
        body = await req.json()
        self.repo_name = body['repository']['full_name']
        repo_url = 'github.com'+self.repo_name

    async def get_data_from_request(self, req: Request):
        body = await req.json()
        event_type = req.headers.get('X-GitHub-Event')
        sender = body['sender']['login']
        repo_name = body['repository']['full_name']
        repo_url = 'github.com'+repo_name
        event_url = None #TODO
        if event_type == ('pull_reqeust' or 'issue' or 'push'):
            event_url = body[event_type]['html_url']

        return AnalyzedWebHookResponse(
            sender, event_type, repo_name, repo_url, event_url
        )


    async def return_bot_data(self): pass

    async def __change_tier(self): pass
