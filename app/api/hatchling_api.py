from fastapi import APIRouter

hatchling_bot = APIRouter()


@hatchling_bot.post('/')  # 이름 정하기
def bot_initial_setting(): pass


@hatchling_bot.post('/{name}/github/event')  # 깃 허브 웹훅 주소
def git_event(name: str): pass


@hatchling_bot.get('/{name}/github/status') #연동된 깃허브 주소
def git_status(name: str): pass


@hatchling_bot.get('/{name}/status')  # 봇 커밋수로 결정된 등급과 이름 보여주기
def bot_status(name: str): pass
