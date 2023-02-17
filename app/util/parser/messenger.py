from app.core.messenger.api.payload import MessagePayload
from app.util.random_value import generate_random_secret


def payload_to_message(payload: MessagePayload):
    entry = payload.entry[0]['messaging'][0]

    return {
        'secret': message if (message := entry['message'].get('text')) is not None else generate_random_secret(),
        'sender': entry['sender']['id'],
    }
