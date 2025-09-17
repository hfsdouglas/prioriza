from marshmallow import Schema, fields, validate

class CreateTaskSchema(Schema):
    task = fields.Str(required=True, validate=validate.Length(min=10))