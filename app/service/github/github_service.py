from abc import ABC, abstractmethod

from .github_service_impl import GithubServiceImpl


class GithubService(ABC):

    @staticmethod
    @abstractmethod
    def when_ping(bot_id: str, body: dict): return GithubServiceImpl.when_ping(bot_id, body)

    @staticmethod
    @abstractmethod
    def when_issue(bot_id: str, body: dict): return GithubServiceImpl.when_issue(bot_id, body)

    @staticmethod
    @abstractmethod
    def when_pr(bot_id: str, body: dict): return GithubServiceImpl.when_pr(bot_id, body)
