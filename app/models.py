from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from flask_login import UserMixin

class User(UserMixin, db.Model):
    '''
    Class that defines the user object template
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True, index=True)
    qualities = db.relationship('Quality', backref='user', lazy = 'dynamic')

    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute!')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Quality(db.Model):
    '''
    Class that defines the user object template
    '''
    __tablename__='qualities'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    complexion = db.Column(db.String(10))
    personality = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
