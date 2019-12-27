from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.types import ChoiceType
from Models.Models import db, guard
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    # firstname = db.Column(db.String(50), nullable=False)
    # lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False,unique=True)
    password = db.Column(db.String(500), nullable=False)
    joined = db.Column(db.DateTime())
    roles = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True, server_default='true')

    def __init__(self, username: str, password: str,roles: str,is_active: bool):
        # self.firstname = firstname.title()
        # self.lastname = lastname.title()
        self.username = username.lower()
        self.joined = datetime.now()
        self.password = guard.hash_password(password)
        self.roles = roles
        self.joined = datetime.now()
        self.is_active = is_active

    def checkpassword(self, password):
        return guard.hash_password(password) == self.password

    def __repr__(self):
        return "< {0} {1} {2}>".format(self.id, self.username, 'user')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active
