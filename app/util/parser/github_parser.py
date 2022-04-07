class GithubParser:

    @staticmethod
    def get_repository_name(request: dict):
        return {
            'repo_name': request['repository']['full_name']
        }

    @staticmethod
    def parse_issues(request: dict):
        return {
            'repo_name': request['repository']['full_name'],
            'action': request['action'],
            'html_url': request['issue']['html_url'],
            'sender': request['sender']['login']
        }

    @staticmethod
    def parse_pr(request: dict):
        return {
            'repo_name': request['repository']['full_name'],
            'action': request['action'],
            'html_url': request['pull_request']['html_url'],
            'sender': request['sender']['login']
        }