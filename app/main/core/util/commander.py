from abc import ABC, abstractmethod
from app.main.core.util.webhook_parser import Parser
from app.main.core.util.message_sender import MessageSender
from app.main.core.util.sql_executer import SqlExecuter


class Commander(ABC):
    @abstractmethod
    def __init__(self, parser: Parser, message_sender: MessageSender, recoder: SqlExecuter): pass


class CommanderImpl(Commander):

    def __init__(self, parser: Parser, message_sender: MessageSender, recoder: SqlExecuter):
        self.parser = parser
        self.message_sender = message_sender
        self.recoder = recoder

    def webhook(self): pass
    # get commit amt and change tier
    # parser webhook data
    # save repo name and url
    # sand message to client

    def __change_bot_tier(self): pass
    # check repo where bot_id = id
    # if commit_amt > 200 tier -> B
    # if commit_amt > 400 tier -> A
    # if commit_amt > 600 tier -> S

    def get_bot_information(self): pass
    # get bot information
    # 개인 또는 동아리 -> 레포
    # 개인이 -> 페북 페이제 메시지
    # 단펨에서 -> 페이지 페메
