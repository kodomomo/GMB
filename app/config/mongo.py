import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = int(os.environ['MONGO_PORT'])
MONGO_DATABASE = os.environ['MONGO_DATABASE']