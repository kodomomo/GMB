class Repository:

    def __init__(self, full_name: str, public: bool):
        self.__name = full_name
        self.__url = 'github.com/' + self.__name
        self.__private = public
        self.__event_amt = 0

    def get_name(self): return self.__name

    def get_url(self): return self.__url

    def is_public(self): return self.__private

    def get_event_amt(self): return self.__event_amt
