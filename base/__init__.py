import os
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

cors = CORS(resources={r"/v1/*": {"origins": "*"}})  # enable CORS for all routes
db = SQLAlchemy()
migrate = Migrate(compare_type=True)

login = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db)
    login.init_app(app)
    login.login_view = 'login'
    # register page folders as blueprints
    from home import home as home_bp
    app.register_blueprint(home_bp)
    # log to files
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/pedi.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    return app
