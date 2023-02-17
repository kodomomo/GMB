from fastapi import HTTPException


class TypeNotJsonException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail='WEBHOOK DATA TYPE IS NOT JSON'
        )


class SecurityHeaderNotExistException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail='SECURITY HEADER IS NOT SET'
        )


class IncorrectSecurityException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail='SECURITY IS NOT CORRECT'
        )
