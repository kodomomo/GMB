from typing import List

from pymongo import MongoClient, ASCENDING
from pymongo.database import Database, Collection
from pymongo.errors import CollectionInvalid

from app.config.mongo import MONGO_HOST, MONGO_PORT, MONGO_DATABASE, MONGO_USER_NAME, MONGO_PASSWORD
from app.core.data.mongo.collections import CollectionNames
from app.core.data.mongo.pending_webhook import PendingWebhook


class Select:
    TRUE = 1
    FALSE = 0


def get_mongo_db(user_name: str, password: str, host: str, port: int, database: str) -> Database:
    mongodb = MongoClient(
        f'mongodb://{user_name}:{password}@{host}:{port}',
        document_class=dict,
        tz_aware=False
    ).get_database(database)

    return mongodb


def get_collection(collection_name: str) -> Collection:
    return mongo.get_collection(collection_name)


def initialize_collections(db: Database, collection_names: List[str]):
    for name in collection_names:

        try:
            db.create_collection(name)

        except CollectionInvalid:
            pass


def set_ttl(db: Database, collection_name: str, document_name: str, ttl_sec: int):
    create_index(
        db, collection_name, document_name, ttl_sec=ttl_sec
    )


def create_index(db: Database, collection_name: str, document_name: str, ttl_sec: int):  # TODO
    collection = db.get_collection(collection_name)
    collection.create_index(
        [(document_name, ASCENDING)], expireAfterSeconds=ttl_sec
    )


def init_mongo():
    initialize_collections(mongo, CollectionNames.NAME_LIST)
    set_ttl(mongo, CollectionNames.PENDING_WEBHOOK, PendingWebhook.CREATED_AT, 60 * 10)


mongo = get_mongo_db(
    MONGO_USER_NAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DATABASE
)
