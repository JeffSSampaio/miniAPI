import json
from src.models import Usuario
from src.extensions import db

def test_create_usuario(client):
    response = client.post("/api/usuarios/", json={
        "nome": "Matheus",
        "email": "matheus@email.com"
    })

    data = response.get_json()
    assert "id" in data
    assert data["nome"] == "Matheus"
    assert data["email"] == "matheus@email.com"


def test_create_usuario_invalido(client):
    response = client.post("/api/usuarios/", json={})
    assert response.status_code == 400


def test_get_usuarios(client):
    user = Usuario(nome="Alice", email="alice@gmail.com")
    db.session.add(user)
    db.session.commit()

    response = client.get("/api/usuarios/")
    lista = response.get_json()
    assert len(lista) == 1
    assert lista[0]["nome"] == "Alice"


def test_update_usuario(client):
    user = Usuario(nome="Bob", email="bob@gmail.com")
    db.session.add(user)
    db.session.commit()

    response = client.put(f"/api/usuarios/{user.id}/", json={"nome": "Bob Novo"})
    data = response.get_json()

    assert data["nome"] == "Bob Novo"


def test_update_usuario_inexistente(client):
    response = client.put("/api/usuarios/999/", json={})
    data = response.get_json()
    assert data["message"] == "Usuário não encontrado"


def test_delete_usuario(client):
    user = Usuario(nome="Carlos", email="carlos@gmail.com")
    db.session.add(user)
    db.session.commit()

    response = client.delete(f"/api/usuarios/{user.id}/")
    data = response.get_json()

    assert data["message"] == "Usuário deletado"


def test_delete_usuario_inexistente(client):
    response = client.delete("/api/usuarios/999/")
    data = response.get_json()
    assert data["message"] == "Usuário não encontrado"
