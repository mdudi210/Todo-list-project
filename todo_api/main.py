from fastapi import FastAPI, HTTPException
from typing import List
from models import Task , TaskCreate
from api_functions import ApiFunctions
from config import Config

app = FastAPI()

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return ApiFunctions.load_tasks()


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    return ApiFunctions.create_task(task)


@app.put("/tasks/{task_id}/done", response_model=Task)
def mark_task_done(task_id: str):
    updated_task = ApiFunctions.mark_task_done(task_id)
    if updated_task:
        return updated_task
    raise HTTPException(status_code=404, detail=Config.NOT_FOUND)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    success = ApiFunctions.delete_task(task_id)
    if success:
        return {Config.MSG: Config.DELETE_MSG}
    raise HTTPException(status_code=404, detail=Config.NOT_FOUND)