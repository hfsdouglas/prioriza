from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    email = fields.Email()
    password = fields.Str(required=True, validate=validate.Length(min=6))