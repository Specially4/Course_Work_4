from marshmallow import Schema, fields

from db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    favorite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
