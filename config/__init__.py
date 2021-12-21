import os


class Config:
    HOST = os.environ['HOST'],
    PORT = 3306,
    CHARSET = os.environ['CHARSET'],
    USER = os.environ['USER'],
    PASSWORD = os.environ['PASSWORD']
