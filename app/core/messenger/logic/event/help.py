from app.util.request.messenger import send_message
from app.util.parser.messenger import Message


def handle_help(message: Message):
    message_text = r"Here is a tutorial link you can follow!\n" \
                      r"github.com/Kodomomo/GMB/blob/master/README.md\n"\
                      r"Thank you!!"

    send_message(
        recipient_id=message.sender,
        message_text=message_text
    )

