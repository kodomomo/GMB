from fastapi.datastructures import Headers

from hashlib import sha256
from hmac import new, compare_digest

from app.common.exception import throw
from app.common.exception.github import SecurityHeaderNotExistException, IncorrectSecurityException


def check_security_set(header: Headers):
    return security_header \
        if (security_header := header.get('X-Hub-Signature-256')) is not None\
        else throw(SecurityHeaderNotExistException)


def check_security_correct(security: str, security_header: str, payload: dict):
    security = security.encode()
    signature = new(security, payload, sha256).hexdigest()

    print(compare_digest('sha256=' + signature, security_header))