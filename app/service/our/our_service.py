from ...util.db.decorater.db_decorater import select_all_repository_by_event_amt


class OurService:

    @staticmethod
    @select_all_repository_by_event_amt
    def show_rank(): pass
