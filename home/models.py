from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from base import db
from base.function_pool import get_time
from passlib.apps import custom_app_context as pwd_context

from config import Config
from flask_login import UserMixin


class Billing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(150))
    fire_token = db.Column(db.String(200))
    ip = db.Column(db.String(30))
    created = db.Column(db.String(20), default=get_time())
    active = db.Column(db.SMALLINT, default=1)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=15768000):  # expires in 6 months
        s = Serializer(Config.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    def invalidate_token(self, expiration=3600):
        s = Serializer(Config.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': 0})

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(Config.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        return '<Profile {}>'.format(self.uid)
