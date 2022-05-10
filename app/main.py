from app import create_app

from .service.our import our_provide_service

app = create_app()

@app.get('/')
def show_repository_lank(): return our_provide_service['show_rank']()