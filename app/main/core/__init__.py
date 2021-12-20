from util import create_gateway
from .main_bot import MainBotImpl


def create_commander(name: str, tier: str):
    gate_way = create_gateway()

    commander = MainBotImpl(name, tier, gate_way)

    return commander
