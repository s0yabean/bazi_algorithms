"""Initialize app."""
from flask import Flask, abort, url_for, redirect
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from flask_session import Session, SqlAlchemySessionInterface
from .cache import cache
from flask_wtf.csrf import CSRFProtect
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
import os

patch_all()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    
    if os.getenv('FLASK_ENV') == 'development':
        app.config.from_object('config.DevConfig')
        print("inside loop")
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/tony/database/prod.db"
    elif os.getenv('FLASK_ENV') == 'production':
        app.config.from_object('config.ProdConfig')

    print(app.config['SQLALCHEMY_DATABASE_URI'])

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    app.config['SESSION_SQLALCHEMY'] = db
    sess = Session()
    sess.init_app(app)

    csrf = CSRFProtect()
    csrf.init_app(app)

    admin = Admin(app, 'Admin Area', template_mode='bootstrap3')
    
    with app.app_context():
        from . import routes
        from .auth import auth
        from .landing import landing
        from .demo import demo
        from .timeline import timeline
        from .network import network
        from .legal import legal
        from .blog import blog
        from .payment import payment
        from .assets.assets import compile_static_assets
        from .persistence.models import User, NatalChart, ExternalPillars

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(demo.demo_bp)
        app.register_blueprint(landing.landing_bp)
        app.register_blueprint(timeline.timeline_bp)
        app.register_blueprint(network.network_bp)
        app.register_blueprint(legal.legal_bp)
        app.register_blueprint(blog.blog_bp)
        app.register_blueprint(payment.pay_bp)

        # Remove protection for Stripe webhooks
        csrf.exempt(payment.pay_bp)

        # Create Database Models
        db.create_all()

        # Create customized model view class
        class MyModelView(ModelView):
            def is_accessible(self):
                if not current_user.is_active or not current_user.is_authenticated:
                     return False
                return current_user.email == "tonytongwa@gmail.com"
            
            def _handle_view(self, name, **kwargs):
                if not self.is_accessible():
                    abort(500)
 
        class NatalChartView(MyModelView):
            column_list = ("id","user_id",'contact_name',"hour_s","hour_e", "day_s", "day_e", "month_s", "month_e", "year_s", "year_e")
            form_columns = ("id", "user_id",'contact_name',"hour_s","hour_e", "day_s", "day_e", "month_s", "month_e", "year_s", "year_e")
        class UserView(MyModelView):
            column_list = ('name','email', 'natal_chart_id', 'plan')
        admin.add_view(UserView(User, db.session))
        admin.add_view(NatalChartView(NatalChart, db.session))
        admin.add_view(MyModelView(ExternalPillars, db.session))

        # Compile static assets
        compile_static_assets(app)

        return app



