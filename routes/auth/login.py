from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route('/login', methods=['POST'])
def login():
    return "Login route"