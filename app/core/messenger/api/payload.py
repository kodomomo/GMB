from pydantic import BaseModel


class MessagePayload(BaseModel):
    object: str
    entry: list
