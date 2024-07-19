from flask import Flask
from flask_sqlalchemy import *

app = Flask(__name__)

app.secret_key = b'hahhahahahaahaha'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kitaplik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_name = db.Column(db.String(80), nullable=False)


with app.app_context():
    db.create_all()

