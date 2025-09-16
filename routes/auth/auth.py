from flask import Blueprint, jsonify, request, redirect
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required

from routes.auth.schemas import LoginSchema
from routes.auth.schemas import SignInSchema

from database.db import db

from models.user import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route('/login', methods=['POST'])
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
                "name": user.name,
                "email": user.email
            }
        )

        response = jsonify({
            "message": f"Olá, {user.name.title()}! Seja bem-vindo ao Prioriza!",
            "token": token
        })

        set_access_cookies(response, token)    
        
        return response
    except ValidationError as error:
        return jsonify(error.messages), 400

@auth.route('/signin', methods=['POST'])
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
    
@auth.route("/protected")
@jwt_required()
def protected():
    return jsonify(foo="bar")

