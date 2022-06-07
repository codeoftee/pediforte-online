import os
import pathlib


class Config(object):
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEV_MODE = False
    SQLALCHEMY_POOL_RECYCLE = 499
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(
        pathlib.Path().absolute(), 'pediforte_online.db'
    )
