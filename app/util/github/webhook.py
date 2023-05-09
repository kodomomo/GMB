from fastapi.datastructures import Headers

from hashlib import sha256
from hmac import new, compare_digest


def check_security_set(header: Headers):
    return security_header \
        if (security_header := header.get('X-Hub-Signature-256')) is not None \
        else None  # TODO


def check_security_correct(security: str, security_header: str, payload: bytes):
    security = security.encode('utf-8')
    signature = new(security, payload, sha256).hexdigest()

    if not compare_digest('sha256=' + signature, security_header):
        raise  # TODO
