from collections import defaultdict

from app.core.github.logic.event.issue import handle_issue_event
from app.core.github.logic.event.non_operate import handle_none_provide_event
from app.core.github.logic.event.ping import handle_ping_event
from app.core.github.logic.event.pull_request import handle_pull_request_event
from app.core.github.logic.event.push import handle_push_event

event_handler_dictionary = defaultdict(lambda: handle_none_provide_event)

event_handler_dictionary['ping'] = handle_ping_event
event_handler_dictionary['push'] = handle_push_event
event_handler_dictionary['issue'] = handle_issue_event
event_handler_dictionary['pull_request'] = handle_pull_request_event
