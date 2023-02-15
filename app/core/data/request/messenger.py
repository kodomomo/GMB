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


PENDING_MESSAGE = r"ℹ️ HOW TO USE\n\n\n" \
                  r"1️⃣ 해당 Repository > Settings > Webhooks > Add Webhook\n\n" \
                  r"2️⃣ Payload URL : https://20d5-168-188-234-72.ngrok.io/{webhook_id} \n\n" \
                  r"3️⃣ Content type : application/json \n\n" \
                  r"4️⃣ Secret : {secret} \n\n\n" \
                  r"=========================\n\n" \
                  r"⛔️ 보안을 위해 Secret을 설정해주세요. ⛔️\n" \
                  r"⛔️ Content type != json 일 경우 작동하지 않습니다. ⛔️"
