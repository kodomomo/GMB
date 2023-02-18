def parse_ping_event(payload: dict):
    return {
        'github_id': payload['sender']['id'],
        'github_name': payload['sender']['login'],
        'repository_id': payload['repository']['id'],
        'repository_name': payload['repository']['name'],
        'repository_url': payload['repository']['url'],
    }
