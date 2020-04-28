from marshmallow import fields, validate
from .. import db, ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.TIMESTAMP,
                              default=db.func.current_timestamp(),
                              nullable=False)
    modification_date = db.Column(db.TIMESTAMP,
                                  default=db.func.current_timestamp(),
                                  onupdate=db.func.current_timestamp(),
                                  nullable=False)


class UserSchema(ma.Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    password = fields.String(required=True,
                             validate=[validate.Length(min=6, max=20)])
    creation_date = fields.DateTime()
    modification_date = fields.DateTime()
