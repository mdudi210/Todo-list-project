import requests
from collections import defaultdict

API_URL = "http://127.0.0.1:8000"

def show_menu():
    print("""\n ===== TODO List CLI =====
1. View all tasks
2. View done tasks
3. View not done tasks
4. Add a task
5. Mark a task as done
6. Delete a task
7. Exit 
""")
    

def view_tasks(filter_by=None):
    response = requests.get(f"{API_URL}/tasks")
    if response.status_code == 200:
        tasks = response.json()
        grouped_tasks = defaultdict(list)

        if filter_by == "done":
            tasks = [task for task in tasks if task["is_done"]]
        elif filter_by == "not_done":
            tasks = [task for task in tasks if not task["is_done"]]

        if not tasks:
            print("\nNo tasks found")
            return
        
        for task in tasks:
            created_at = task["created_at"]
            date_part = created_at.split(" ")[0].strip()
            grouped_tasks[date_part].append(task)

        for date, tasks_on_date in grouped_tasks.items():
            print(f"\n===== Tasks added on {date} =====")
            for task in tasks_on_date:
                status = "Done" if task["is_done"] else "Not Done"
                print(f"\nID: {task["id"]}\nTitle: {task["title"]}\nDesc: {task["description"]}\nStatus: {status}\nCreated At: {task["created_at"]}\n")

    else:
        print("Error fetching tasks!")


def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    data = {
        "title": title,
        "description": description
    }
    response = requests.post(f"{API_URL}/tasks", json=data)
    if response.status_code == 200:
        print("Task added successfully!")
    else:
        print("Failed to add task!")


def mark_done():
    task_id = input("Enter task ID to mark as done: ")
    response =  requests.put(f"{API_URL}/tasks/{task_id}/done")
    if response.status_code == 200:
        print("Task marked as done")
    else:
        print("Task not found")


def delete_task():
    task_id = input("Enter task Id to delete: ")
    confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").lower()
    if confirm != "y":
        print("Deletion cancelled")
        return
    
    response = requests.delete(f"{API_URL}/tasks/{task_id}")
    if response.status_code == 200:
        print("task deleted successfully")
    else:
        print("Task not found or could not be deleted")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            view_tasks(filter_by="done")
        elif choice == "3":
            view_tasks(filter_by="not_done")
        elif choice == "4":
            add_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again ")


if __name__ == "__main__":
    main()
