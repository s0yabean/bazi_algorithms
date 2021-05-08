"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from flask_session import Session
from .cache import cache
from flask_wtf.csrf import CSRFProtect

patch_all()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    app.config['SESSION_SQLALCHEMY'] = db
    sess = Session()
    sess.init_app(app)

    csrf = CSRFProtect()
    csrf.init_app(app)

    with app.app_context():
        from . import routes
        from .auth import auth
        from .landing import landing
        from .demo import demo
        # from .crm import crm
        # from .accounts import accounts
        # from .mbti_content import mbti_content
        from .assets.assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(landing.landing_bp)
        # app.register_blueprint(demo.demo_bp)
        # app.register_blueprint(mbti_content.mbti_content_bp)
        # app.register_blueprint(crm.crm_bp)
        # app.register_blueprint(accounts.accounts_bp)

        # Create Database Models
        # Seems like just need to create once, and then don't run it anymore.
        # db.create_all()

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app



