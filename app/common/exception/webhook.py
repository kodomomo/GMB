from fastapi import HTTPException


class WebhookNotFoundException(HTTPException):
    def __init__(self, detail = 'WEBHOOK IS NOT EXIST'):
        super().__init__(
            status_code=404,
            detail=detail
        )
