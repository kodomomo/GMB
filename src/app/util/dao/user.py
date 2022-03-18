from sqlalchemy import Column, VARCHAR, ForeignKey

from ..dao import Base


class UserModel(Base):
    __tablename__ = 'user'

    psid = Column('psid', VARCHAR(250), primary_key=True)
    bot_id = Column('bot_id', VARCHAR(250), ForeignKey('bot.bot_id'), nullable=True)

    def __init__(self,psid):
        self.psid = psid
