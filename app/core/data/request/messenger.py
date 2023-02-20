from requests import post


def send_message(
        page_access_token: str,
        recipient_id: str,
        message_text: str,
        message_type: str = "MESSAGE_TAG",
        tag: str = "CONFIRMED_EVENT_UPDATE"
):
    recipient = "{id : " + recipient_id + "}"
    message = "{'text' : '" + message_text + "'}"

    post(
        url=f"https://graph.facebook.com/v16.0/me/messages?" \
            f"access_token={page_access_token}&" \
            f"recipient={recipient}&" \
            f"message={message}&" \
            f"message_type={message_type}&" \
            f"tag={tag}",
        headers={"Content-Type": "application/json"},
    )


PENDING_MESSAGE = r"✅ How to use\n\n" \
                  r"    · https://github.com/Kodomomo/GMB\n\n\n\n" \
                  r"✅ Redirect URL\n\n" \
                  r"    · {base_url}/github/webhook/{id_}"
