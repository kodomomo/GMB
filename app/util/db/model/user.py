from ..model import Base

from sqlalchemy import Column, VARCHAR, DATETIME, ForeignKey

from uuid import uuid4

from datetime import datetime


class User(Base):
    __tablename__ = 'user'

    psid = Column(VARCHAR(250), primary_key=True)
    bot_id = Column(VARCHAR(250), nullable=False, default=uuid4(),primary_key=True)
    repo_name = Column(VARCHAR(150), ForeignKey('repository.repo_name'), nullable=True)
    registered_at = Column(DATETIME, nullable=False)

    def __init__(self, psid: str):
        self.psid = psid
        self.bot_id = uuid4()
        self.registered_at = datetime.now().replace(microsecond=0)