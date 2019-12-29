import os
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_heroku import Heroku
from Models import db, guard
from Models import User
from utils import tampared


config = {
    "dev": "config.Development",
    "prod": "config.Production"
}

blacklist = set()

def is_blacklisted(jti):
    return jti in blacklist



class create_app():
    app = Flask(__name__)
    cors = CORS(app)
    migrate = Migrate(app, db)
    heroku = Heroku(app)
    def __init__(self):
        env = os.getenv("ENV")
        self.app.config.from_object(config.get(env))
        db.init_app(self.app)
        guard.init_app(self.app, User, is_blacklisted=is_blacklisted)

        ##    # Register Jinja template functions
        ##    from .utils import register_template_utils
        ##    register_template_utils(app)
        ##
        ##    # Set up asset pipeline
        ##    assets_env = Environment(app)
        ##    dirs = ['assets/styles', 'assets/scripts']
        ##    for path in dirs:
        ##        assets_env.append_path(os.path.join(basedir, path))
        ##    assets_env.url_expire = True
        ##
        ##    assets_env.register('app_css', app_css)
        ##    assets_env.register('app_js', app_js)
        ##    assets_env.register('vendor_css', vendor_css)
        ##    assets_env.register('vendor_js', vendor_js)
        ##
        ##    # Configure SSL if platform supports it
        ##    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        ##        from flask_sslify import SSLify
        ##        SSLify(app)

        # Create app blueprints
        from .main import main as main_blueprint
        self.app.register_blueprint(main_blueprint)
