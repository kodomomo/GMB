from app.core.messenger.api.payload import MessagePayload
from app.util.time import timestamp_to_datetime


def message_payload_to_message(payload: MessagePayload):
    entry = payload.entry[0]['messaging'][0]

    return {
        'content': entry['message'].get('text'),
        'sender': entry['sender']['id'],
        'receipt': entry['recipient']['id'],
        'send_at': timestamp_to_datetime(entry['timestamp'])
    }
