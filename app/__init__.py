from flask import Flask


def register_bp(app: Flask):
    from .external_api.github import github_bp

    app.register_blueprint(github_bp)


def create_app() -> Flask:
    app = Flask("Kodomo-Dragon")

    register_bp(app)

    return app
