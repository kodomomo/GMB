from fastapi import APIRouter, Request
from app.main.core import create_hatchling_bot

bot_router = APIRouter()


@bot_router.post('/bot')
async def create_new_bot():
    hatchling_bot = create_hatchling_bot()

@bot_router.post('/bot/{name}')
async def get_github_event(req: Request): pass


@bot_router.get('/bot/{name}')
async def get_bot_status(): pass


@bot_router.delete('/bot/{name')
async def delete_bot(): pass
