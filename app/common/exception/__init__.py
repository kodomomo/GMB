from fastapi import HTTPException


def throw(exc):
    assert issubclass(exc, HTTPException) and issubclass(exc, Exception), 'IT IS NOT A EXCEPTION'
    raise exc
