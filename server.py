import os
from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from datetime import timedelta

from database.db import db
from routes.routes import register_routes
from libs.jwt import jwt_instance

def create_app(test_config=None):
    app = Flask(__name__)

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'Prioriza API',
        'description': 'Prioriza é uma API simples e poderosa para gerenciamento de tarefas. Com ela, você pode cadastrar usuários, criar e organizar tarefas, definir prioridades e acompanhar o progresso diretamente na sua aplicação. ⚡📂',
        'version': '1.0.0',
        'uiversion': 3,
        'specs_route': '/docs/'
    }

    # Configurações do JWT
    app.config["JWT_SECRET_KEY"] = "prioriza_secret_asdkjfaj293dr012973wejll"
    app.config["JWT_COOKIE_SECURE"] = True
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    # Caminho absoluto do diretório onde está este arquivo
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Pasta do banco de dados
    DB_DIR = os.path.join(BASE_DIR, "database")
    os.makedirs(DB_DIR, exist_ok=True)  # cria a pasta se não existir

    # Caminho completo do arquivo SQLite
    DB_PATH = os.path.join(DB_DIR, "prioriza.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    register_routes(app)

    swagger = Swagger(app)
    jwt = jwt_instance(app)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)