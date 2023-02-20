def get_action(reqeust: dict):
    return reqeust['action']


def parse_pull_request(request: dict):
    return {
        'url': request['pull_request']['html_url'],
        'title': request['pull_request']['title'],
        'user': request['pull_request']['user']['login'],
        'repository': request['repository']['name']
    }
