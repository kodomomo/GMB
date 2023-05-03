from app.model.pending_webhook import PendingWebhook
from app.model.webhook.webhook import Webhook


def pending_webhook_to_webhook(pending_webhook: PendingWebhook):
    return Webhook(

    )