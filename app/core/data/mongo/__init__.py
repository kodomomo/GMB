from typing import List

from pymongo import MongoClient, ASCENDING, IndexModel
from pymongo.database import Database, Collection
from pymongo.errors import CollectionInvalid
# from pymongo.typings import _DocumentType as DocumentType

from app.common.exception import throw
from app.common.exception.mongodb import DatabaseNotFoundException

from app.config.mongo import MONGO_HOST, MONGO_PORT, MONGO_DATABASE
from app.core.data.mongo.collections import CollectionNames
from app.core.data.mongo.pending_webhook import PendingWebhook


class Select:
    TRUE = 1
    FALSE = 0


def get_mongo_db(host: str, port: int, database: str) -> Database:
    mongodb = MongoClient(
        host=host,
        port=port,
        document_class=dict,
        tz_aware=False
    ).get_database(database)

    # 익셉션 처리가 아니라, 새로운 db에서 작동하게 해야할까? TODO

    return mongodb if len(mongodb.list_collection_names()) != 0 else throw(DatabaseNotFoundException)


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
    MONGO_HOST, MONGO_PORT, MONGO_DATABASE
)
