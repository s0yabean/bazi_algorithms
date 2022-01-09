"""Flask app configuration."""
import os


class Config:
    """Base config."""

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')

    # Flask-SQLAlchemy
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Assets
    LESS_BIN = os.getenv('LESS_BIN')
    ASSETS_DEBUG = os.getenv('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = os.getenv('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = os.getenv('COMPRESSOR_DEBUG')

    # Flask Sessions
    # SESSION_TYPE = environ.get("sqlalchemy")
    SESSION_TYPE = "sqlalchemy"
    # When SESSION_PERMANENT is False, close the browser (not close the tab), and the session becomes invalid.
    # On the contrary, when SESSION_PERMANENT is True, the session becomes invalid after the time set by PERMANENT_SESSION_LIFETIME.
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_USE_SIGNER = True  # security feature


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')
    # If you intend your app to be reachable on a custom domain, we specify the app's domain name here.
    # SERVER_NAME =


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI')
