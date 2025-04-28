import requests
from collections import defaultdict
from config import Config

def show_menu():
    print(Config.MENU)
    

def view_tasks(filter_by=None):
    response = requests.get(f"{Config.API_URL}/tasks")
    if response.status_code == 200:
        tasks = response.json()
        grouped_tasks = defaultdict(list)

        if filter_by == Config.DONE :
            tasks = [task for task in tasks if task[Config.IS_DONE]]
        elif filter_by == Config.NOT_DONE :
            tasks = [task for task in tasks if not task[Config.IS_DONE]]

        if not tasks:
            print(Config.NO_TASK_FOUND)
            return
        
        for task in tasks:
            created_at = task[Config.CREATED_AT]
            date_part = created_at.split(" ")[0].strip()
            grouped_tasks[date_part].append(task)

        for date, tasks_on_date in grouped_tasks.items():
            print(f"\n {Config.TASK_ADDED} {date} ")
            for task in tasks_on_date:
                status = Config.DONE if task[Config.IS_DONE] else Config.NOT_DONE
                print(f"\nID: {task["id"]}\nTitle: {task["title"]}\nDesc: {task["description"]}\nStatus: {status}\nCreated At: {task[Config.CREATED_AT]}\n")

    else:
        print(Config.ERROR_FETCHING)


def add_task():
    title = input(Config.ENTER_TITLE)
    description = input(Config.ENTER_DESC)
    data = {
        "title": title,
        "description": description
    }
    response = requests.post(f"{Config.API_URL}/tasks", json=data)
    if response.status_code == 200:
        print(Config.TASK_ADDED)
    else:
        print(Config.FAILED_ADD_TASK)


def mark_done():
    task_id = input(Config.ENTER_ID_TO_MARK_DONE)
    response =  requests.put(f"{Config.API_URL}/tasks/{task_id}/done")
    if response.status_code == 200:
        print(Config.TASK_MARKED_DONE)
    else:
        print(Config.TASK_NOT_FOUND)


def delete_task():
    task_id = input(Config.ENTER_ID_TO_DELETE)
    confirm = input(f"{Config.SURE_DELETE} {task_id} {Config.Y_N}").lower()
    if confirm != "y":
        print(Config.CANCELLED)
        return
    
    response = requests.delete(f"{Config.API_URL}/tasks/{task_id}")
    if response.status_code == 200:
        print(Config.TASK_DELETED)
    else:
        print(Config.TASK_NOT_FOUND_OR_DELETED)


def main():
    while True:
        show_menu()
        choice = input(Config.ENTER_CHOICE).strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            view_tasks(filter_by=Config.DONE)
        elif choice == "3":
            view_tasks(filter_by=Config.NOT_DONE)
        elif choice == "4":
            add_task()
        elif choice == "5":
            mark_done()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            print(Config.EXIT)
            break
        else:
            print(Config.INVALID_CHOICE)


if __name__ == "__main__":
    main()
