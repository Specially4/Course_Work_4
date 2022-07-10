from marshmallow import fields, Schema

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    __tablename__ = 'genre'
    id = fields.Integer()
    name = fields.String()


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
