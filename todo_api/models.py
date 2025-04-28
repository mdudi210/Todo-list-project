from pydantic import BaseModel

class Task(BaseModel):
    id: str
    title: str
    description: str
    created_at : str
    is_done : bool 

class TaskCreate(BaseModel):
    title: str
    description: str