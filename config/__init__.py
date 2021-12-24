import os


class DbConfig:
    HOST = os.environ['HOST']
    PORT = int(os.environ['PORT'])
    USER = os.environ['USER']
    PASSWORD = os.environ['PASSWORD']
    CHARSET = os.environ['CHARSET']

