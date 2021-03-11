from sqlalchemy.orm import backref
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    name = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    loaned = db.Column(db.Boolean, default=False, nullable=False)
    date_loaned = db.Column(db.DateTime, default=None)

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return '<Book %r>' % self.name


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref='client', lazy=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Client %r>' % self.name