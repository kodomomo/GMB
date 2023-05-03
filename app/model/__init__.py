from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.model.webhook.webhook import Webhook
from app.model.pending_webhook import PendingWebhook

from app.config.mongo import MongoConfig


async def init_mongodb():
    client = AsyncIOMotorClient(MongoConfig.MONGO_URL)
    database = getattr(client, MongoConfig.DB_NAME)

    await init_beanie(database=database, document_models=[Webhook, PendingWebhook])
