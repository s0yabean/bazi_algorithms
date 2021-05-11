"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from flask_session import Session
from .cache import cache
from flask_wtf.csrf import CSRFProtect
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

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

    admin = Admin(app)

    with app.app_context():
        from . import routes
        from .auth import auth
        from .landing import landing
        from .demo import demo
        from .timeline import timeline
        from .assets.assets import compile_static_assets
        from .persistence.models import User, NatalChart, ExternalPillars

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(landing.landing_bp)
        app.register_blueprint(timeline.timeline_bp)

        # Create Database Models
        db.create_all()

        admin.add_view(ModelView(User, db.session))
        admin.add_view(ModelView(NatalChart, db.session))
        admin.add_view(ModelView(ExternalPillars, db.session))

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app



