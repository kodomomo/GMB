from message_sender import MessageSenderImpl
from webhook_parser import ParserImpl
from recorder import RecoderImpl


def create_parts():
    parser = ParserImpl()
    sender = MessageSenderImpl()
    recoder = RecoderImpl()

    return {
        'parser': parser,
        'sender': sender,
        'recoder': recoder
    }
