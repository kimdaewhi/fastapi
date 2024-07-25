from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 인메모리 DB
todos = []

class Todo(BaseModel):
    id: int
    title: str
    desc: Optional[str] = None
    complete: bool = False

# Create(POST)
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# Read(GET) - 전체 리스트 조회
@app.get("/todos/", response_model=List[Todo])
def read_todos():
    return todos

# Read(GET) - 특정 할 일 조회
@app.get("todos/", response_model=Todo)
def read_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    
    raise HTTPException(status_code=404, detail="Todo not found")

# Delete(DELETE)
@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo
        
    raise HTTPException(status_code=404, detail="Todo not found")