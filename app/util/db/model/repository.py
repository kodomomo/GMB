from ..model import Base
from sqlalchemy import Column, Integer, VARCHAR


class Repository(Base):
    __tablename__ = 'repository'

    repo_name = Column(VARCHAR(150), primary_key=True)
    url = Column(VARCHAR(200), nullable=False)
    event_amt = Column(Integer, nullable=False)

    def __init__(self, repo_name: str):
        self.repo_name = repo_name
        self.url = 'github.com/' + repo_name
        self.event_amt = 0
