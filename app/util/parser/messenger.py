from app.core.messenger.api.payload import MessagePayload


def payload_to_message(payload: MessagePayload):
    entry = payload.entry[0]['messaging'][0]

    return {
        'content': entry['message'].get('text'),
        'sender': entry['sender']['id'],
        'receipt': entry['recipient']['id'],
    }
