from marshmallow import Schema, fields, validate

class CreateTaskSchema(Schema):
    task = fields.String(required=True, validate=validate.Length(min=10))

class UpdateTaskSchema(Schema):
    task = fields.String(required=True, validate=validate.Length(min=10))
    user_id = fields.UUID(required=True)
    completed = fields.Boolean(required=True)