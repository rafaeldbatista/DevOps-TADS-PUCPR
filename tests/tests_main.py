from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "mensagem" in response.json()


def test_listar_todos_vazio():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_criar_todo():
    todo = {
        "id": 1,
        "tarefa": "Estudar DevOps no feriado ",
        "concluida": False
    }
    response = client.post("/todos", json=todo)
    assert response.status_code == 200
    assert response.json()["tarefa"] == "Estudar DevOps durante a semana"


def test_obter_todo_existente():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_obter_todo_inexistente():
    response = client.get("/todos/999")
    assert response.status_code == 404