from app.core.messenger.logic.event.pending_webhoook import initialize_pending_hook
from app.core.messenger.logic.event.info import handle_info
from app.core.messenger.logic.event.help import handle_help
from app.core.messenger.logic.event.hello import handle_hello

# Type 정적으로 관리하면 좋을 것 같다 TODO
# 함수 추상화를 위해서 추상 클래스를 만들고 handle_function 만든 다음에 구현 클래스에서 정적으로 만드록 접근해도 괜찮을 것 같다. TODO

__tutorial_type = {
    'hello': True,
    'info': True,
    'help': True,
}

__tutorial_handler = {
    'hello': handle_hello,
    'info': handle_info,
    'help': handle_help,
}

get_handler_by_type = lambda x: __tutorial_handler[x] if __tutorial_type.get(x) else initialize_pending_hook
