from abc import ABCMeta, abstractmethod
from fastapi import Request
from .payload.response import *


class Hatchling(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def parse_webhook_event(self, req): pass

    @abstractmethod
    def change_tier(self): pass

    @abstractmethod
    def return_bot_data(self): pass
