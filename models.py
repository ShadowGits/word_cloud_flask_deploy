from flask import Flask
from marshmallow import fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Image(db.Model):
    __tablename__="Images"
    id = db.Column(db.Integer, primary_key=True)
    encoded_image= db.Column(db.String)

class ImageSchema(ma.Schema):
    id = fields.Integer()
    encoded_image = fields.String(required=True)


class TextInput(db.Model):
    __tablename__="CloudPreData"
    id = db.Column(db.Integer, primary_key=True)
    text_for_cloud= db.Column(db.String)

class TextInputSchema(ma.Schema):
    id = fields.Integer()
    text_for_cloud = fields.String(required=True)

