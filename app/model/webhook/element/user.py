from pydantic import BaseModel


class User(BaseModel):
    github_id: str
    github_name: str

    messenger_id: str