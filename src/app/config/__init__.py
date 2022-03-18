import os


class Config:
    DB_URL = os.getenv('DB_URL')
