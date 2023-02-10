from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

APP_ID = environ['MESSENGER_APP_ID']
APP_SECRET = environ['MESSENGER_APP_SECRET']

MESSENGER_WEBHOOK_VERIFY_TOKEN = environ['MESSENGER_WEBHOOK_VERIFY_TOKEN']
REDIRECT_URI = 'https://ac1a-168-188-240-208.jp.ngrok.io/facebook/redierect'
STATE = environ['STATE']
PAGE_ID = environ['PAGE_ID']
