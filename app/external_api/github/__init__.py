from flask import Blueprint, request

from ...service.github import act_service_by_type

github_bp = Blueprint('github', __name__, url_prefix='/github')


@github_bp.post('/<bot_id>')
def get_webhook_by_each_bot(bot_id):
    event_type = request.headers.get('X-Github-Event')
    body = request.get_json()

    return act_service_by_type[event_type](bot_id, body)
