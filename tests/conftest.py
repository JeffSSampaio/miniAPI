import pytest
from src.app import create_app
from src.extensions import db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        # Limpa o banco antes de cada teste
        db.drop_all()
        db.create_all()

        yield app.test_client()

        # Limpa tudo após o teste
        db.session.remove()
        db.drop_all()
