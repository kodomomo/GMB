from sqlalchemy import Column, VARCHAR, INTEGER

from ..dao import Base


class RepositoryModel(Base):
    __tablename__ = 'repository'

    repo_name = Column('repo_name', VARCHAR(150), primary_key=True)
    url = Column('url', VARCHAR(250), nullable=False)
    event_amt = Column('event_amt', INTEGER, nullable=False)

    def __init__(self, full_name):
        self.repo_name = full_name
        self.url = 'github.com/' + full_name
        self.event_amt = 0
