from app import create_app

from app.service.our import our_service

from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = create_app()
templates = Jinja2Templates(directory="/Volumes/Tools/Project/Python/Kodomo-Dragon/app/templates")


@app.get('/', response_class=HTMLResponse)
def show_repository_lank(request: Request):
    return templates.TemplateResponse('table.html', context={
        'request': request,
        'repo_list': our_service['show_rank']()
    })
