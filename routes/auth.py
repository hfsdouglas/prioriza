from flask import Blueprint, jsonify, request, redirect
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token 
from flasgger import swag_from

from schemas.auth import LoginSchema
from schemas.auth import SignInSchema

from docs.auth.auth_specs import AuthSpecs

from database.db import db

from models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route('/login', methods=['POST'])
@swag_from(AuthSpecs.login_specs())
def login():
    schema = LoginSchema()

    try:
        data = schema.load(request.json)

        user = User.query.filter_by(email=data["email"], password=data["password"]).first()

        if not user:
            return jsonify({"message": "Credenciais inválidas"}), 401
        
        token = create_access_token(
            identity=user.id, 
            additional_claims={
                "id": user.id,
                "name": user.name,
                "email": user.email
            },
        )

        name = user.name.split(" ")[0].title()

        response = jsonify({
            "message": f"Olá, {name}! Seja bem-vindo ao Prioriza!",
            "token": token
        })

        return response
    except ValidationError as error:
        return jsonify(error.messages), 400

@auth_bp.route('/signin', methods=['POST'])
@swag_from(AuthSpecs.signin_specs())
def signin():
    schema = SignInSchema()

    try:
        data = schema.load(request.json)

        new_user = User(
            name = data["name"],
            email = data["email"],
            password = data["password"]
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect('/login', code=301)
    except ValidationError as error:
        return jsonify(error.messages), 400