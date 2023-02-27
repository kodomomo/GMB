import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MESSENGER_WEBHOOK_VERIFY_TOKEN = os.environ['MESSENGER_WEBHOOK_VERIFY_TOKEN']
PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']