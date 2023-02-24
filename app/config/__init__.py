import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BASE_URL = os.environ['BASE_URL']