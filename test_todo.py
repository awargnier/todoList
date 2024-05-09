
from fastapi.testclient import TestClient

from main import app
import pytest


client = TestClient(app)

from router.router_todo import Todo
todoList = [
  Todo(todo="faire le mapping"),
  Todo(todo="3 x 4")
]

def test_get_todo():
  response = client.get("/")
  assert response.status_code == 200

def test_post_todo():
  response = client.post("/", json={"todo": "Buy groceries"})
  assert response.status_code == 405
  # assert todoList.append(new_todo)

def test_get_todoId_valid():
  response = client.get("/1")
  assert response.status_code == 404

def test_get_todoId_invalid():
  response = client.get("/3")  
  assert response.status_code == 404  

def test_update_todo():
  update_data = {"todo": "Updated task"}
  response = client.put("/1", json=update_data)
  assert response.status_code == 404

def test_update_todo_invalid():
  update_data = {"todo": "Updated task"}
  response = client.put("/3", json=update_data)  
  assert response.status_code == 404  

def test_delete_todo():
  response = client.delete("/1")
  assert response.status_code == 404

def test_delete_todo_invalid():
  response = client.delete("/3")  # Non-existent ID
  assert response.status_code == 404  # Expect Not Found