from flask import jsonify
from flask_jwt_extended import JWTManager; 

def jwt_instance(app):
    jwt = JWTManager(app)

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
    
    return jwt
