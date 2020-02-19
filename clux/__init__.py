import os

from flask import Flask
from flask import request
from flask_babelex import Babel
from flask_images import Images
import flask_wtf
from clux.db import db_cli
from clux.auth import AuthManager
from clux.admin import AdminManager
from clux.views import index
from clux.api import api_bp

LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

def create_app(config=None):

    app = Flask(__name__, instance_relative_config=True)
    flask_wtf.CSRFProtect(app)
    images = Images(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if config is None:
        from config import Config
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(config)

    auth = AuthManager(app)
    admin_manager = AdminManager(app)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Setup Babel
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(LANGUAGES.keys())

    app.register_blueprint(index.index_bp)
    app.register_blueprint(api_bp)

    # Add command 'flask db migrate' or other 'flask db'
    app.cli.add_command(db_cli)
    
    return app