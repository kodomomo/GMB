from ...util.db.decorater.db_decorater import create_bot,assign_bot, increase_event_amount


class GithubService:

    @staticmethod
    @create_bot
    @assign_bot
    def when_ping(bot_id: str, type: str, body: dict) -> dict:
        return body

    @staticmethod
    @assign_bot
    @increase_event_amount
    def when_issue(bot_id: str, type: str, body: dict): pass

    @staticmethod
    @assign_bot
    @increase_event_amount
    def when_pr(bot_id: str, type: str, body: dict): pass

    @staticmethod
    @assign_bot
    @increase_event_amount
    def when_push(bot_id: str, type: str, body: dict): pass