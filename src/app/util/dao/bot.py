from sqlalchemy import Column, VARCHAR, DATETIME, ForeignKey

from uuid import uuid4
from datetime import datetime

from ..dao import Base


class BotModel(Base):
    __tablename__ = 'bot'

    bot_id = Column('bot_id', VARCHAR(250), primary_key=True)
    repo_name = Column('repo_name', VARCHAR(150), ForeignKey('repository.repo_name'), nullable=True)
    created_at = Column('created_at', DATETIME, nullable=False)

    def __init__(self):
        self.bot_id = uuid4()
        self.created_at = datetime.now().replace(microsecond=0)
