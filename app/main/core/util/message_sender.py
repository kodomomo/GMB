from abc import ABC, abstractmethod
import requests

class MessageSender(ABC):
    pass


class MessageSenderImpl(MessageSender):

    def send(self): pass

