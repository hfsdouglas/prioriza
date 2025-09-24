import pytest

from server import create_app

from database.db import db
from models.user import User

@pytest.fixture
def app():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def sample_user(app):
    with app.app_context():
        user = User(
            name="John Doe",
            email="johndoe@email.com",
            password="123456"
        )
        
        db.session.add(user)
        db.session.commit()

         # refresh para garantir que está salvo e tem ID
        db.session.refresh(user)

        # expurga da sessão -> agora pode ser usado sem erro
        db.session.expunge(user)

        # return {"id": user.id, "nome": user.name, "email": user.email, "password": user.password}
        return user