from util.commander import Commander


class MainBot:

    def __init__(self, name: str, tier: str, commander: Commander):
        self.name = name
        self.tier = tier
        self.commander = commander

