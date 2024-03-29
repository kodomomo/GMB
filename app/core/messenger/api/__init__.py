from fastapi import Request, APIRouter
from app.core.messenger.api.payload import MessagePayload

from app.config import MessengerConfig
from app.core.messenger.logic.event import get_handler_by_type
from app.util.parser.messenger import payload_to_message

messenger_router = APIRouter(
        prefix='/messenger'
)


@messenger_router.get('/webhook')
def verify_this_endpoint(request: Request):
    query_params = dict(request.query_params)

    assert query_params['hub.verify_token'] == MessengerConfig.MESSENGER_WEBHOOK_VERIFY_TOKEN

    return int(query_params['hub.challenge'])


@messenger_router.post('/webhook')
def handle_message(message: MessagePayload):

    parsed_message = payload_to_message(message)

    handle_function = get_handler_by_type(parsed_message.content.lower())

    handle_function(parsed_message)

