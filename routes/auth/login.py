from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from routes.auth.schemas import LoginSchema

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route('/login', methods=['POST'])
def login():
    schema = LoginSchema()

    try:
        data = schema.load(request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400
    
    return jsonify({
        "message": "Seja bem-vindo ao Prioriza!",
        "token": "seu_token_aqui"
    }), 200