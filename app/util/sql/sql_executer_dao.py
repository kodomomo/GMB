class CreateBotDAO:
    def __init__(self, name: str, psid: str, repository_name: str):
        self.__name = name
        self.__psid = psid
        self.__repository_name = repository_name

    def get_field_variable_as_dict(self):
        return {
            'name': self.__name,
            'psid': self.__psid,
            'repository_name': self.__repository_name
        }


class CreateRepositoryDAO:
    def __init__(self, name: str, url: str, is_public: bool, event_amt: int):
        self.__name = name
        self.__url = url
        self.__is_public = is_public
        self.__event_amt = event_amt

    def get_field_variable_as_dict(self):
        return {
            'name': self.__name,
            'url': self.__url,
            'is_public': self.__is_public,
            'event_amt': self.__event_amt
        }


class UpdateRepositoryNameInBotDAO:

    def __init__(self, repository_name: str, bot_id: str):
        self.__repository_name = repository_name
        self.__bot_id = bot_id

    def get_field_variable_as_dict(self):
        return {
            'repository_name': self.__repository_name,
            'bot_id': self.__bot_id
        }


class UpdateEventAmountDAO:

    def __init__(self, repo_name: str, event_amt: int):
        self.__repo_name = repo_name
        self.__event_amt = event_amt

    def get_field_variable_as_dict(self):
        return {
            'repo_name': self.__repo_name,
            'event_amt': self.__event_amt
        }
