import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class GMBConfig:
    BASE_URL = os.environ['BASE_URL']


class MongoConfig:
    _MONGO_HOST = os.environ['MONGO_HOST']
    _MONGO_PORT = os.environ['MONGO_PORT']
    _MONGO_ROOT_NAME = os.environ['MONGO_ROOT_NAME']
    _MONGO_ROOT_PASSWORD = os.environ['MONGO_ROOT_PASSWORD']

    DB_NAME = os.environ['MONGO_DATABASE_NAME']
    MONGO_URL = f'mongodb://{_MONGO_ROOT_NAME}:{_MONGO_ROOT_PASSWORD}@{_MONGO_HOST}:{_MONGO_PORT}'


class MessengerConfig:
    PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']
    MESSENGER_WEBHOOK_VERIFY_TOKEN = os.environ['MESSENGER_WEBHOOK_VERIFY_TOKEN']
