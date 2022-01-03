from fastapi import APIRouter

bot_router = APIRouter()


@bot_router.get('/{bot_id}')
def get_bot_id(): pass
