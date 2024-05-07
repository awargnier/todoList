from fastapi import APIRouter

from pydantic import BaseModel

router= APIRouter(
    prefix='/todo',
    tags=["Todo"]
)

class Todo(BaseModel):
  todo: str


todoList = [
  Todo(todo="faire le mapping"),
  Todo(todo="3 x 4")
]

@router.get('/')
async def get_todo():
  return todoList

@router.post('/')
async def post_todo(todo: Todo):
  todoList.append(todo)
  return todo

@router.get('/{id}')
async def get_todoId(id: int):
  return todoList[id-1]

@router.put('/{id}')
async def update_todo(id: int, todo: Todo):
  todoList[id-1] = todo
  return "success"

@router.delete('/{id}')
async def get_todoId(id: int):
  todoList.remove(todoList[id-1])
  return "success"
