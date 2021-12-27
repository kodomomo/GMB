from abc import ABC, abstractmethod
from pymysql.cursors import DictCursor
from config import DbConfig
import pymysql


class SqlExecuter(ABC): pass


class SqlExecuterImpl(SqlExecuter):

    def __init__(self, host, port, user, password, charset):
        self.__db = pymysql.connect(
            host=host,
            port=port,
            charset=charset,
            database='kodomo_dragon',
            autocommit=True,
            user=user,
            password=password
        )
        self.cursor = self.__db.cursor(DictCursor)

    def show_bot_and_relation_repository(self, bot_id: str):
        bot = self.__select_bot_by_bot_id(bot_id)
        return {
            'bot': bot,
            'repository': self.__select_repository_by_repo_full_name(bot['repo_name'])
        }

    def create_bot(self, name: str, psid: str, repo_name: str):
        uuid = "unhex(replace(uuid(),'-',''))"
        self.cursor.execute(
            f'insert into bot(id,name,created_at,psid,repo_name) values ({uuid},"{name}",now(),"{psid}","{repo_name}");'
        )

    def create_repo(self, full_name: str, is_public: bytes, event_amt: int):
        url = 'github.com/' + full_name
        self.cursor.execute(
            f'insert into repository(id,url,is_public,event_amt) values("{full_name}","{url}",{is_public},{event_amt})'
        )

    def update_repo_name(self, repo_name: str, bot_id: str):
        self.cursor.execute(
            f'UPDATE bot set repo_name="{repo_name}" where id={bot_id};'
        )

    def update_repo_event_amt(self, repo_name: str, event_amt: int):
        self.cursor.execute(
            f'update repository set event_amt="{event_amt}" where id="{repo_name}";'
        )

    def __select_bot_by_bot_id(self, bot_id: str):
        bot = 'None Bot'
        self.cursor.execute(
            f'select * from bot where id={bot_id};'
        )
        bot = self.cursor.fetchone()
        return bot

    def __select_repository_by_repo_full_name(self, repo_name: str):
        repository = 'None Repository'
        if repo_name is not None:
            self.cursor.execute(
                f'select * from repository where id="{repo_name}";'
            )
            repository = self.cursor.fetchone()
        return repository


if __name__ == '__main__':
    a = SqlExecuterImpl(
        DbConfig.HOST,
        DbConfig.PORT,
        DbConfig.USER,
        DbConfig.PASSWORD,
        DbConfig.CHARSET
    )

    #a.create_bot('name', 'psid', 'repo_name')
    #a.create_repo('repo_name', 1, 0)
    #a.update_repo_name('dhdhdhdhdhdhdhd','0x9D4D2DD8667911ECA3F26A6BD7F64D9C')
    #print(a.show_bot_and_relation_repository('0x787BEE8666EC11ECA3F26A6BD7F64D9C'))
    a.update_repo_event_amt('repo_name',6000)