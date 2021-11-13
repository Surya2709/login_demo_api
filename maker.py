from flask import Flask

from api.rest.login import USER_BLUEPRINT


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(USER_BLUEPRINT)
    
    return app
