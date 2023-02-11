from fastapi import Request, APIRouter
from app.core.facebook.api.webhook.payload import MessagePayload

from app.config.messenger import MESSENGER_WEBHOOK_VERIFY_TOKEN
from app.core.facebook.logic import classify_service
from app.util.parser.messenger import message_payload_to_message

messenger_router = APIRouter(
    prefix='/facebook'
)


@messenger_router.get('/webhook')
def verify_this_endpoint(request: Request):
    query_params = dict(request.query_params)

    assert query_params['hub.verify_token'] == MESSENGER_WEBHOOK_VERIFY_TOKEN

    return int(query_params['hub.challenge'])


@messenger_router.post('/webhook')
async def handle_message(message: MessagePayload):
    message = message_payload_to_message(message)

    return classify_service(message)
