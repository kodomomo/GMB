from collections import defaultdict

from app.core.github.logic.event.issue import handle_issue_event
from app.core.github.logic.event.non_operate import handle_none_provide_event
from app.core.github.logic.event.ping import handle_ping_event
from app.core.github.logic.event.pull_request import handle_pull_request_event
from app.core.github.logic.event.push import handle_push_event

event_handler_dictionary = defaultdict(lambda: handle_none_provide_event)


class EventType:
    PING = 'ping'
    PUSH = 'push'
    ISSUE = 'issue'
    PULL_REQUEST = 'pull_request'


event_handler_dictionary[EventType.PING] = handle_ping_event
event_handler_dictionary[EventType.PUSH] = handle_push_event
event_handler_dictionary[EventType.ISSUE] = handle_issue_event
event_handler_dictionary[EventType.PULL_REQUEST] = handle_pull_request_event
