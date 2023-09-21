from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))

class List(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150))

# class GunineWeb(db.Model,UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     list = db.Column(db.String(150))