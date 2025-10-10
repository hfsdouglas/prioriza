import os
from flask import Flask

from database.db import db
from libs.jwt import jwt_instance
from libs.swagger import swagger_instance

from routes.auth import auth_bp
from routes.tasks import tasks_bp

def create_app(test_config=None):
    app = Flask(__name__)
    
    jwt_instance(app)
    swagger_instance(app)

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

    # Registra os blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)