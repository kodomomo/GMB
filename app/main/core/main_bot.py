from abc import ABC, abstractmethod
from .part.webhook_parser import Parser
from .part.message_sender import MessageSender
from .part.recorder import Recoder


class Hatchling(ABC):
    @abstractmethod
    def __init__(self, parser: Parser, message_sender: MessageSender, recoder: Recoder): pass


class HatchlingImpl(Hatchling):

    def __init__(self, parser: Parser, message_sender: MessageSender, recoder: Recoder):
        self.parser = parser
        self.message_sender = message_sender
        self.recoder = recoder



