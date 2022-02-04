import pymysql
from pymysql.cursors import DictCursor
from config import DbConfig

from app.util.sql.entity.repository import Repository



def create_repositoryDAO():

    repository_dao_impl = RepositoryDAOImpl()


class RepositoryDAOImpl:

    def __init__(self, config: DbConfig):
        self.__db = pymysql.connect(
            host=config.HOST,
            port=config.PORT,
            user=config.USER,
            password=config.PASSWORD,
            charset=config.CHARSET,
            database='gmb',
            autocommit=True,
        )
        self.__cursor = self.__db.cursor(DictCursor)

    def new_repository(self,repository: Repository):
        self.__cursor.execute(
            f'insert into repository values("{repository.get_name()}","{repository.get_url()}","{int(repository.is_public())}", 0);'
        )


    def increase_event_amt(self,name):
        self.__cursor.execute(
            f'select event_amt + 1 as amt from repository where name="{name}"'
        )
        amt = self.__cursor.fetchone()
        self.__cursor.execute(
            f'update repository set event_amt={amt["amt"]} where name="{name}"'
        )
        #서브 쿼리로 나중에 바꿔주기

    def reverse_public(self,name):
        self.__cursor.execute(
            f'select private from repository where name="{name}"'
        )
        reversed_bool = False if self.__cursor.fetchone().get('private') else True
        self.__cursor.execute(
            f'update repository set private={reversed_bool} where name="{name}"'
        )

    def find_repository_by_name(self,repository_name: str):
        self.__cursor.execute(
            f'select * from repository where name="{repository_name}"'
        )
    #TODO 이름 수정 & URL 수정 & 삭제


if __name__ == '__main__':
    dbconfig = DbConfig()
    rep = RepositoryDAOImpl(dbconfig)

    print(rep.reverse_public('name'))