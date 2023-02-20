def get_type(request: dict):
    return request['action']


def parse_issue(request: dict):
    return {
        'url': request['issue']['html_url'],
        'title': request['issue']['title'],
        'user': request['issue']['user']['login'],
        'repository_name': request['repository']['name'],
    }