from fastapi import Request

from app.core.messenger.api import messenger_router
from app.core.messenger.api.webhook.payload import MessagePayload

from app.config.messenger import MESSENGER_WEBHOOK_VERIFY_TOKEN


@messenger_router.get('/webhook')
def verify_this_endpoint(request: Request):
    query_params = dict(request.query_params)

    assert query_params['hub.verify_token'] == MESSENGER_WEBHOOK_VERIFY_TOKEN

    return int(query_params['hub.challenge'])


@messenger_router.post('/webhook')
async def handle_message(message: MessagePayload):
    print(message.object)
    from pprint import pprint

    pprint(message.entry)
