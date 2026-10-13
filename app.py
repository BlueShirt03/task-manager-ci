from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    completed: bool = False

app = FastAPI()
tasks = {}
next_task_id = 1

@app.get("/")
def home():
    return{"message": "Welcome to the Task Manager API"}

@app.get("/tasks")
def get_task():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_task_id

    task_id = next_task_id
    tasks[task_id] = task.model_dump()
    next_task_id += 1

    return {"id": task_id, **tasks[task_id]}