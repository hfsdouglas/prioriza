from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_current_user
from sqlalchemy.orm import selectinload
from marshmallow import ValidationError
from flasgger import swag_from
from uuid import UUID

from database.db import db

from schemas.task import CreateTaskSchema, UpdateTaskSchema

from docs.tasks.task_specs import Task_Specs

from models.user import User
from models.tasks import Task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.post("/tasks")
@jwt_required()
@swag_from(Task_Specs.create_task_specs())
def create_task():
    schema = CreateTaskSchema()

    try:
        data = schema.load(request.json)

        user = get_current_user()

        task = Task(
            task = data['task'],
            user_id = user.id
        )

        db.session.add(task)
        db.session.commit()

        return jsonify({
            "message": "Tarefa cadastrada com sucesso!"
        })

    except ValidationError as error:
        return jsonify(error.messages), 400
    
@tasks_bp.patch('/tasks/<task_id>')
@jwt_required()
@swag_from(Task_Specs.update_task_specs())
def update_task(task_id):
    schema = UpdateTaskSchema()

    try:
        data = schema.load(request.json)

        user = User.query.filter_by(id=data['user_id']).first()

        if not user:
            return jsonify({
                "message": "Usuário não encontrado!"
            }), 400
        
        task = Task.query.filter_by(id=task_id).first()

        if not task: 
            return jsonify({
                "message": "Tarefa não encontrada!"
            }), 404
        
        task.task = data['task']
        task.completed = data['completed']
        task.user_id = data['user_id']

        db.session.commit()

        return jsonify({
            "message": "Tarefa atualizada com sucesso!"
        })
    except ValidationError as error: 
        return jsonify(error.messages), 400
    
@tasks_bp.delete('/tasks/<int:task_id>')
@jwt_required()
@swag_from(Task_Specs.delete_task_specs())
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()

    if not task: 
        return jsonify({
            "message": "Tarefa não encontrada!"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Tarefa deletada com sucesso!"
    })

@tasks_bp.get('/tasks/<int:task_id>')
@jwt_required()
@swag_from(Task_Specs.get_task_specs())
def get_task_by_id(task_id):
    task = Task.query.filter_by(id=task_id).first()

    if not task: 
        return jsonify({
            "message": "Tarefa não encontrada!"
        }), 404

    return jsonify({
        "id": str(task.id),
        "description": task.task,
        "completed": task.completed,
        "user": {
            "id": str(task.user.id),
            "name": task.user.name
        }
    }), 200

@tasks_bp.get('/tasks')
@jwt_required()
@swag_from(Task_Specs.get_tasks_specs())
def get_tasks():
    users = (
        User.query
            .options(selectinload(User.tasks))
            .all()
    )

    data = []

    for user in users: 
        data.append({
            "user_id": user.id,
            "user_name": user.name, 
            "user_email": user.email,
            "user_tasks": [
                {
                    "task_id": task.id, 
                    "description": task.task, 
                    "completed": task.completed
                } for task in user.tasks 
            ]
        })

    return jsonify(data)

@tasks_bp.get('/users/<uuid:user_id>/tasks')
@jwt_required()
@swag_from(Task_Specs.get_task_by_user_specs())
def get_task_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()

    if not user: 
        return jsonify({
            "message": "Usuário não encontrado!"
        }), 404

    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify([
        {"id": str(task.id), "description": task.task, "completed": task.completed}
        for task in tasks
    ])