from uuid import UUID
from fastapi import Request

from app.core.github.logic.event import event_handler_dictionary
from app.util.parser.github import get_event_type


async def act_by_event_type(bot_id: UUID, request: Request):
    payload = await request.json()
    event_type = get_event_type(request)

    handle_function = event_handler_dictionary[event_type]

    await handle_function(bot_id, event_type, payload)