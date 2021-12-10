from pydantic import BaseModel


class BotInit(BaseModel):
    name: str
    rank: str
