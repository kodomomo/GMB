from app import create_app
from app.model import init_mongodb

app = create_app()


@app.on_event('startup')
async def startup_setting():

    await init_mongodb()


if __name__ == '__main__':
    from uvicorn import run

    run(app)