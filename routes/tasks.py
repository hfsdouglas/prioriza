from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.post("/tasks")
@jwt_required()
def create_task():
    return jsonify({
        "message": "foo"
    })