from uuid import UUID
from typing import Optional
from datetime import datetime


class User(dict):
    GITHUB_ID = 'githubId'
    GITHUB_NAME = 'githubName'
    SENDER_ID = 'senderId'

    def __init__(
            self,
            github_id: str,
            github_name: str,
            sender_id: str
    ):
        super().__init__(
            githubId=github_id,
            githubName=github_name,
            senderId=sender_id
        )


class Repository(dict):
    ID = 'repositoryId'
    NAME = 'repositoryName'
    URL = 'repositoryUrl'

    def __init__(
            self,
            repository_url: str,
            repository_name: str,
            repository_id: str,
    ):
        super().__init__(
            repositoryId=repository_id,
            repositoryName=repository_name,
            repositoryUrl=repository_url
        )


class Amt(dict):
    PUSH = 'push'
    ISSUE = 'issue'
    PULL_REQUEST = 'pullRequest'
    NON_PROVIDE = 'nonProvide'

    def __init__(
            self,
            push: int = 0,
            issue: int = 0,
            pull_request: int = 0,
            non_provide: int = 0
    ):
        super().__init__(
            push=push,
            issue=issue,
            pullRequest=pull_request,
            nonProvide=non_provide
        )


class Webhook(dict):
    ID = '_id'
    SECRET = 'secret'
    CRATED_AT = 'createdAt'
    AMT = 'amt'
    USER = 'user'
    REPOSITORY = 'repository'

    class Amt(Amt):
        PUSH = 'amt.' + Amt.PUSH
        ISSUE = 'amt.' + Amt.ISSUE
        PULL_REQUEST = 'amt.' + Amt.PULL_REQUEST
        NON_PROVIDE = 'amt.' + Amt.NON_PROVIDE

    class User(User):
        GITHUB_ID = 'user.' + User.GITHUB_ID
        GITHUB_NAME = 'user.' + User.GITHUB_NAME
        SENDER_ID = 'user.' + User.SENDER_ID

    class Repository(Repository):
        ID = 'repository.' + Repository.ID
        NAME = 'repository.' + Repository.NAME
        URL = 'repository.' + Repository.URL

    def __init__(
            self,
            id_: UUID,
            secret: str,
            amt: Amt,
            user: User,
            repository: Repository,
            created_at: datetime,
    ):
        super().__init__(
            _id=str(id_),
            secret=secret,
            createdAt=created_at,
            user=user,
            amt=amt,
            repository=repository
        )
