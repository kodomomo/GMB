from fastapi import APIRouter, Request

bot_router = APIRouter()


@bot_router.post('/bot')
async def create_new_bot(): pass


@bot_router.post('/bot/{name}')
async def get_github_event(req: Request): pass


@bot_router.get('/bot/{name}')
async def get_bot_status(): pass


@bot_router.delete('/bot/{name')
async def delete_bot(): pass
