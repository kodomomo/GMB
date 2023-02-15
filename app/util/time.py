from datetime import datetime, timedelta


def ktc_now():
    return datetime.utcnow() + timedelta(hours=9)


def utc_now():
    return datetime.utcnow()
