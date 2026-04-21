from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Minha API de Tarefas")

class Todo(BaseModel):
    id: int
    tarefa: str
    concluida: bool = False

# Banco de dados temporário
banco_dados: List[Todo] = []

@app.get("/", tags=["Root"])
def read_root():
    return {"mensagem": "Bem-vindo à API de Tarefas!"}

@app.get("/todos", response_model=List[Todo])
def listar_todos():
    return banco_dados

@app.post("/todos", response_model=Todo)
def criar_todo(todo: Todo):
    banco_dados.append(todo)
    return todo

@app.get("/todos/{todo_id}", response_model=Todo)
def obter_todo(todo_id: int):
    for t in banco_dados:
        if t.id == todo_id:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")