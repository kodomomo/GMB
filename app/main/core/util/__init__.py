from message_sender import MessageSenderImpl
from webhook_parser import ParserImpl
from sql_executer import SqlExecuterImpl
from commander import CommanderImpl


def create_commander():  # TODO 변수명 생각하기
    utils = create_utils()
    main_commander = CommanderImpl(
        utils['webhook_parser'],
        utils['message_sender'],
        utils['sql_executer']
    )
    return main_commander


def create_utils():
    sender = MessageSenderImpl()
    query_executer = SqlExecuterImpl()
    parser = ParserImpl()
    return {
        'message_sender': sender,
        'sql_executer': query_executer,
        'webhook_parser': parser
    }  # TODO 변수명 생각 하기
