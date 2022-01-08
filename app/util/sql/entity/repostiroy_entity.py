class Repository:

    def __init__(self, full_name: str, is_public: bool):
        self.__id = full_name
        self.__url = 'github.com/'+full_name
        self.__is_public = is_public
        self.__event_amount = 0

    def update_event_amount(self):
        self.__event_amount += 1

    def reverse_is_public(self):
        self.__is_public = not self.__is_public

    def get_name(self): return self.__id

    def get_url(self): return self.__url

    def get_is_public(self): return self.__is_public

    def get_event_amt(self): return self.__event_amount
