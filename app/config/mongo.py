from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_HOST = environ['MONGO_HOST']
MONGO_PORT = int(environ['MONGO_PORT'])
MONGO_DATABASE = environ['MONGO_DATABASE']