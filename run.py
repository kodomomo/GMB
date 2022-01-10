from abc import ABC,abstractmethod

from uvicorn import run
from app import create_app

if __name__ == '__main__':
    app = create_app()

    run(app, host='0.0.0.0', port=5000)
