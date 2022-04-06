from ...util.db.decorater.db_decorater import create_new_bot, update_event_amount


class GithubService:
    """
        TODO
        이중 데코레이터의 동작 순서 알아보기
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
    def when_issue(bot_id: str, body: dict) -> dict:

        """
            TODO
            페메 보내는 로직을 데코레이터로 만들어야 함 -- pr의 경우도 마찬가지
        """

        return body

    @staticmethod
    @update_event_amount
    # @notice_by_messenger
    def when_pr(bot_id: str, body: dict) -> dict:

        """
            TODO

        """
        return body
