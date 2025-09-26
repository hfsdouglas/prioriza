from flask import jsonify
from flask_jwt_extended import JWTManager
from datetime import timedelta
from uuid import UUID

from database.db import db

from models.user import User

def jwt_instance(app):
    jwt = JWTManager(app)

    # Configurações do JWT
    app.config["JWT_SECRET_KEY"] = "prioriza_secret_asdkjfaj293dr012973wejll"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # Respostas customizadas para erros de JWT
    # Token expirado
    @jwt.expired_token_loader
    def expired_token_callback():
        return jsonify({
            "message": "Token expirado, faça login novamente"
        }), 401

    # Token inválido (assinatura inválida, formato errado, etc.)
    @jwt.invalid_token_loader
    def invalid_token_callback():
        return jsonify({
            "message": "Token inválido"
        }), 401

    # Token não fornecido
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "message": "Token não fornecido"
        }), 401
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]

        return db.session.get(User, UUID(identity))
    
    return jwt
