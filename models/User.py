from config import app_active, app_config
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User:
    def __init__(self, email=None, password=None, username=None, id_=None):
        self.email = email
        self.password = password
        self.username = username
        self.id = id_

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
    @classmethod
    def find_by_id(cls, session, name):
        x = session.query(cls).filter_by(id=name).all()
        if x:
            return x[0]
        return User()

    @classmethod
    def find_by_email(cls, session, email):
        x = session.query(cls).filter_by(email=email).all()
        if x:
            return x[0]
        return None