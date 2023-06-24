from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    phone_no = db.Column(db.Integer)
    gender = db.Column(db.String(45))
    password = db.Column(db.String(45))
    text = db.relationship('Text') 

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(10000), nullable=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    message_source = db.Column(db.String(45), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
