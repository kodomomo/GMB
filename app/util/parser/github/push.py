def parse_push(request: dict):
    return {
        'name': request['repository']['name'],
        'url': request['repository']['html_url'],
        'commit_amt': len(request['commits'])
    }