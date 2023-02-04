from fastapi import FastAPI, Request
from pydantic import BaseModel

from messenger.config import MESSENGER_WEBHOOK_VERIFY_TOKEN

messenger_app = FastAPI()


@messenger_app.get('/webhook')
def verify_this_endpoint(request: Request):
    query_params = dict(request.query_params)

    assert query_params['hub.verify_token'] == MESSENGER_WEBHOOK_VERIFY_TOKEN  # TODO CustomException

    return int(query_params['hub.challenge'])


class MessagePayload(BaseModel):
    object: str
    entry: list


@messenger_app.post('/webhook')
async def handle_message(message: MessagePayload):

    print(message.object)
    from pprint import pprint

    pprint(message.entry)
