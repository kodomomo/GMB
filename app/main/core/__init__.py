from .part import create_parts
from main_bot import Hatchling


def create_hatchling_bot() -> Hatchling:
    parts = create_parts()

    parser = parts['parser']
    sender = parser['sender']
    recoder = parts['recoder']

    hatchling = Hatchling(parser, sender, recoder)

    return hatchling
