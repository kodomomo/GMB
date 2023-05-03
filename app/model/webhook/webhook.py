from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field

from app.model.webhook.element.amount import Amount
from app.model.webhook.element.reposiotry import Repository
from app.model.webhook.element.user import User


class Webhook(Document):
    id: UUID = Field(default_factory=uuid4)

    user: User
    amt: Amount
    repository: Repository

