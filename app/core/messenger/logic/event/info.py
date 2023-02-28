from app.core.data.request.messenger import send_message
from app.util.parser.messenger import Message


def handle_info(message: Message):
    message_text = r"This is the simple service\nwhich handle repository\nevent by webhook.\n\n" \
                   r"Thank you for using\n\n" \
                   r"         - osangu"

    send_message(
        recipient_id=message.sender,
        message_text=message_text
    )
