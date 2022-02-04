from app.util.sql.entity.repository import Repository


class Bot:

    def __init__(self, name: str, repository: Repository, psid: str):
        self.__name = name
        self.__repository = repository
        self.__psid = psid

    def get_name(self): return self.__name

    def get_psid(self): return self.__psid

    def get_repository(self) -> Repository: return self.__repository
