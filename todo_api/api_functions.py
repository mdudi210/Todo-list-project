import json
import os
from datetime import datetime
from typing import List
from models import Task, TaskCreate
from config import Config

class ApiFunctions:

    def load_tasks() -> List[Task]:
        if not os.path.exists(Config.DATA_FILE):
            return []
        with open(Config.DATA_FILE, "r") as file:
            return [Task(**task) for task in json.load(file)]


    def save_tasks(tasks: List[Task]):
        with open(Config.DATA_FILE, "w") as file:
            json.dump([task.dict() for task in tasks], file, indent=4)


    def get_next_id(tasks: List[Task]) -> int:
        if not tasks:
            return 1
        return max(int(task.id) for task in tasks) + 1


    def create_task(task_data: TaskCreate) -> Task:
        tasks = ApiFunctions.load_tasks()
        new_task = Task(
            id=str(ApiFunctions.get_next_id(tasks)),
            title=task_data.title,
            description=task_data.description,
            created_at=datetime.utcnow().strftime(Config.DATE_FORMATE),
            is_done=False
        )
        tasks.append(new_task)
        ApiFunctions.save_tasks(tasks)
        return new_task


    def mark_task_done(task_id: str) -> bool:
        tasks = ApiFunctions.load_tasks()
        for task in tasks:
            if task.id == task_id:
                task.is_done = True
                ApiFunctions.save_tasks(tasks)
                return task
        return None
            

    def delete_task(task_id: str) -> bool:
        tasks = ApiFunctions.load_tasks()
        updated_tasks = [task for task in tasks if task.id != task_id]
        if len(tasks) == len(updated_tasks):
            return False
        ApiFunctions.save_tasks(updated_tasks)
        return True
        
