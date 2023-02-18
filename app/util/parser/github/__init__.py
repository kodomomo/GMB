from fastapi import Request


def get_event_type(request: Request):
    return request.headers.get('X-GitHub-Event')


