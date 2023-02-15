from fastapi import Request, APIRouter
from app.core.messenger.api.payload import MessagePayload

from app.config.messenger import MESSENGER_WEBHOOK_VERIFY_TOKEN
from app.core.messenger.logic import initialize_pending_hook

messenger_router = APIRouter(
        prefix='/messenger'
)


@messenger_router.get('/webhook')
def verify_this_endpoint(request: Request):
    query_params = dict(request.query_params)

    assert query_params['hub.verify_token'] == MESSENGER_WEBHOOK_VERIFY_TOKEN

    return int(query_params['hub.challenge'])


@messenger_router.post('/webhook')
async def handle_message(message: MessagePayload):
    initialize_pending_hook(message)

