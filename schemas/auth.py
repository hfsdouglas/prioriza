from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str(required=True, validate=validate.Length(min=6))

class SignInSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=8))
    email = fields.Email()
    password = fields.Str(required=True, validate=validate.Length(min=6))