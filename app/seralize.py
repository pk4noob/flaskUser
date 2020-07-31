from extensions.extensions import ma
from app.model import User
from marshmallow import validate, fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True, validate=[
                         validate.Length(min=2, max=20)])
    surname = fields.String(required=True, validate=[
                            validate.Length(min=2, max=20)])
    nickname = fields.String(required=True, validate=[
        validate.Length(min=2, max=20)])
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=[
                             validate.Length(min=8, max=20)])

    class Meta:
        model = User
        load_instance = True
