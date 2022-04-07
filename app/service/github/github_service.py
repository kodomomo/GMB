from ...util.db.decorater.db_decorater import create_new_bot, update_event_amount


class GithubService:
    """
    데코리어터를 사용한 이유
            1 : 함수 내부 로직을 보이지 않고 사용할 수 있음 -> githubservice class를 인터페이스 처럼 사용가능 함
            2 : githubservice에 함수의 행동이 아니라 함수 호출 경우를 이름으로 명시할 수 있게함
            3 : 함수는 한 번에 한 가지 역할을 해야하지만, 데코레이터를 통하면 여러가지 일을 진행할 수 있음.
                -> when 함수가 실행하는 게  아니라 데코레이터 함수가 실행시키는 거니까
            4 : 코드가 간결해짐
    """

    @staticmethod
    @create_new_bot
    # @add_repository_for_each_user
    # @notice_by_messenger
    def when_ping(bot_id: str, body: dict) -> dict:
        """
            TODO
            bot_id를 통해서 user 테이블에 repository 추가해줌.
            bot_id로 찾아낸 user 튜플들에 페메를 발송함.
        """

        return body

    @staticmethod
    @update_event_amount
    # @notice_by_messenger
    def when_issue(bot_id: str, body: dict) -> dict: return body

    @staticmethod
    @update_event_amount
    # @notice_by_messenger
    def when_pr(bot_id: str, body: dict) -> dict: return body
