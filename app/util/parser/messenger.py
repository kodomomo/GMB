from app.core.messenger.api.payload import MessagePayload
from app.util.random_value import generate_random_secret


class Message:
    def __init__(self, content: str, sender: str):
        self.content = content
        self.sender = sender


def payload_to_message(payload: MessagePayload) -> Message:
    entry = payload.entry[0]['messaging'][0]
    message = entry['message'].get('text')

    return Message(
        message if message is not None else generate_random_secret(),
        entry['sender']['id']
    )
