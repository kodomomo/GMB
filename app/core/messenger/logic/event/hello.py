from app.core.data.request.messenger import send_message
from app.util.parser.messenger import Message


def handle_hello(message: Message):
    send_message(
        recipient_id=message.sender,
        message_text=r'Hello!\nyou can use below command.\n\nInfo ::  to show our service information.\nHelp :: get tutorial link.\n\nThank you!!'
    )
