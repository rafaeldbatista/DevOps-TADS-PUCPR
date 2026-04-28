from fastapi.testclient import TestClient
from src.main import app, banco_dados

client = TestClient(app)


def setup_function():
    banco_dados.clear()


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_listar_vazio():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_criar_todo():
    todo = {"id": 1, "tarefa": "Teste", "concluida": False}
    response = client.post("/todos", json=todo)
    assert response.status_code == 200


def test_obter_todo():
    client.post("/todos", json={"id": 2, "tarefa": "Outro", "concluida": False})
    response = client.get("/todos/2")
    assert response.status_code == 200


def test_todo_inexistente():
    response = client.get("/todos/999")
    assert response.status_code == 404