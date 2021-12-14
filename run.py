from uvicorn import run
from app import creat_app

app = creat_app()

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=5000)