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

    
PENDING_MESSAGE = '1️⃣ 해당 Repository > Settings > Webhooks > Add Webhoook\n' \
                  '2️⃣ Payload URL : https://3e08-168-188-234-72.jp.ngrok.io/{webhook_id}\n' \
                  '3️⃣ Content type : application/json \n' \
                  '4️⃣ Secret : {secret}\n\n' \
                  '⚠️ 보안을 위해 Secret을 설정해주세요.\n' \
                  '⛔️ Content type != json 일 경우 작동하지 않습니다.'
