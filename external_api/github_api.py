from fastapi import APIRouter

from app.service.github_service import *

github_router = APIRouter()


@github_router.post('/github/{bot_id}')
def get_webhook_from_github(request: Request):

    parser = GitParserImpl()
    bot_dao = BotDAOImpl(DbConfig())
    repo_dao = RepositoryDAOImpl(DbConfig())

    a = GithubServiceImpl(parser,bot_dao,repo_dao)

    a.execute_by_type(request)