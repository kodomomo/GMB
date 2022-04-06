from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session

__engine = create_engine(
    'mysql+pymysql://root:qwer1234@localhost:3306/gmb'
)

__Session = scoped_session(sessionmaker(bind=__engine, autocommit=False, autoflush=False))

__session = __Session()


def get_session():
    return __session
