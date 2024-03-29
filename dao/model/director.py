from marshmallow import Schema, fields

from db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class DirectorSchema(Schema):
    __tablename__ = 'director'
    id = fields.Integer()
    name = fields.String()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
