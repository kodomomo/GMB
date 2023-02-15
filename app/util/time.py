from datetime import datetime, timedelta


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


def ktc_now():
    return datetime.utcnow() + timedelta(hours=9)

def utc_now():
    return datetime.utcnow()