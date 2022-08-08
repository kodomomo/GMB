import os

from app import create_app

from app.service.our.our_service import OurService

from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = create_app()
templates = Jinja2Templates(directory=os.getcwd() + '/app/templates')


@app.get('/rank', response_class=HTMLResponse)
def show_repository_lank(request: Request):
    return templates.TemplateResponse('table.html', context={
        'request': request,
        'repo_list': OurService.show_rank()
    })
