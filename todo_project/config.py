class Config:
    API_URL = "http://127.0.0.1:8000"
    MENU = """\n TODO List CLI 
1. View all tasks
2. View done tasks
3. View not done tasks
4. Add a task
5. Mark a task as done
6. Delete a task
7. Exit 
"""

    DONE = "done"
    NOT_DONE = "not_done"
    IS_DONE = "is_done"
    NO_TASK_FOUND = "\nNo tasks found"
    ENTER_TITLE = "Enter task title: "
    ENTER_DESC = "Enter task description: "
    TASK_NOT_FOUND = "Task not found"
    CREATED_AT = "created_at"
    TASK_ADDED = "Tasks added on"
    ERROR_FETCHING = "Error fetching tasks"
    TASK_ADDED = "Task added successfully"
    FAILED_ADD_TASK = "Failed to add task"
    TASK_MARKED_DONE = "Task marked as done"
    ENTER_ID_TO_MARK_DONE = "Enter task ID to mark as done: "
    ENTER_ID_TO_DELETE = "Enter task Id to delete: "
    SURE_DELETE = "Are you sure you want to delete task"
    Y_N = "? (y/n): "
    CANCELLED = "Deletion cancelled"
    TASK_DELETED = "task deleted successfully"
    TASK_NOT_FOUND_OR_DELETED = "Task not found or could not be deleted"
    ENTER_CHOICE = "Enter your choice: "
    EXIT = "Exiting..."
    INVALID_CHOICE = "Invalid choice! Please try again "