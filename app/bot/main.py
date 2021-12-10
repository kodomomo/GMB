from ..payload.request import *
from .excpetion.excpetions import *


class Hatchling:
    def __init__(self, bot_init: BotInit):
        self.name = bot_init.name
        self.rank = bot_init.rank

    def __check_bot_information(self):
        if (self.name and self.rank) is not None: return True
        raise NoneInformationSetting
