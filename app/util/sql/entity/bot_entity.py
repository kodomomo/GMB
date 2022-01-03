from datetime import datetime
import uuid


class Bot:

    def __init__(self, name: str, psid: str):
        self.__name = name
        self.__psid = psid
        self.__bot_id = uuid.uuid4()
        self.__created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__repo_name = None

    def update_repo_name(self, full_repo_name: str): self.__repo_name = full_repo_name

    def get_psid(self): return self.__psid

    def get_bot_name(self): return self.__name

    def get_repo_name(self): return self.__repo_name

    def get_created_at(self): return self.__created_at

    def get_bot_id(self): return self.__bot_id

