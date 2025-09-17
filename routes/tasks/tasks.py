from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from schemas import CreateTaskSchema

tasks = Blueprint("tasks", __name__, url_prefix="/")

@tasks.route("/task", methods=["POST"])
@jwt_required
def create_task(): 
    schema = CreateTaskSchema()
    
    try:
        data = schema.load(request.json)
        user_id = request.cookies.get('access_token')

        return jsonify({
            "teste": "teste"
        })
    except ValidationError as error:
        return jsonify(error), 400