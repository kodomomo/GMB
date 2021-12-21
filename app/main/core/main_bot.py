from util.commander import Commander


class MainBot:

    def __init__(self, name: str, tier: str, commander: Commander):
        self.name = name
        self.tier = tier
        self.commander = commander

    # 웹훅이 들어올 경우의 함수 하나

    def webhook_comes(self):
        pass  # self.commander


