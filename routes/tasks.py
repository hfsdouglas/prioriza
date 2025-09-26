from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from uuid import UUID

from database.db import db

from schemas.task import CreateTaskSchema, UpdateTaskSchema

from models.user import User
from models.tasks import Task

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.post("/tasks")
@jwt_required()
def create_task():
    schema = CreateTaskSchema()

    try:
        data = schema.load(request.json)

        user = User.query.filter_by(id=data['user_id']).first()

        if user:
            task = Task(
                task = data['task'],
                user_id = data['user_id']
            )

            db.session.add(task)
            db.session.commit()

            return jsonify({
                "message": "Tarefa cadastrada com sucesso!"
            })
        else:
            return jsonify({
                "message": "Usuário não encontrado!"
            }), 400

    except ValidationError as error:
        return jsonify(error.messages), 400
    
@tasks_bp.patch('/tasks/<int:task_id>')
@jwt_required()
def update_task(task_id):
    schema = UpdateTaskSchema()

    try:
        data = schema.load(request.json)

        user = User.query.get(data['user_id'])

        if not user:
            return jsonify({
                "message": "Usuário não encontrado!"
            }), 400
        
        task = Task.query.get(task_id)

        if not task: 
            return jsonify({
                "message": "Tarefa não encontrada!"
            }), 400
        
        task.task = data['task'],
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
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task: 
        return jsonify({
            "message": "Tarefa não encontrada!"
        }), 400

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Tarefa deletada com sucesso!"
    })

@tasks_bp.get('/tasks/<int:task_id>')
@jwt_required()
def get_task_by_id(task_id):
    task = Task.query.get(task_id)

    if not task: 
        return jsonify({
            "message": "Tarefa não encontrada!"
        }), 400

    return jsonify({
        "data": task
    })

@tasks_bp.get('/tasks')
@jwt_required()
def get_tasks():
    task = Task.query.get()

    if not task: 
        return jsonify({
            "message": "Não há nenhuma tarefa cadastrada no momento!"
        }), 200

    return jsonify({
        "data": task
    })

@tasks_bp.get('/users/<uuid:user_id>/tasks')
@jwt_required()
def get_task_by_user(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify({
        "tasks": [
            {"id": str(task.id), "task": task.task, "completed": task.completed}
            for task in tasks
        ]
    })