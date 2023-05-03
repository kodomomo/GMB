from pydantic import BaseModel


class Repository(BaseModel):
    id: str
    url: str
    name: str
    secret: str