from ...util.db.decorater.db_decorater import create_bot,assign_bot, increase_event_amount


class GithubService:
    """
    데코리어터를 사용한 이유
            1 : 함수 내부 로직을 보이지 않고 사용할 수 있음 -> githubservice class를 인터페이스 처럼 사용가능 함
            2 : 데코레이터를 통해 부가적인 일을 수행함으로 함수가 한 가지의 로직을 하는 데 집중할 수 있게 해 줌
            3 : 코드가 간결해짐
    """

    @staticmethod
    @create_bot
    @assign_bot
    def when_ping(bot_id: str, type: str, body: dict) -> dict:
        return body

    @staticmethod
    @assign_bot
    @increase_event_amount
    def when_issue(bot_id: str, type: str, body: dict) -> dict: return body

    @staticmethod
    @assign_bot
    @increase_event_amount
    def when_pr(bot_id: str, type: str, body: dict) -> dict: return body
