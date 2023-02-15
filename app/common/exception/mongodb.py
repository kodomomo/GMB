from fastapi import HTTPException


class DatabaseNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail='DATABASE NOT FOUND IN MONGO'
        )
