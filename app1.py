def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Remove a task")
    print("5. Exit")


def add_task(tasks):
    task_description = input("Enter the task description: ").strip()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "task": task_description, "completed": False})
    print(f"Task added: '{task_description}'")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"[{status}] {task['id']}: {task['task']}")


def mark_task_complete(tasks):
    try:
        task_id = int(input("Enter the task ID to mark as complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task '{task['task']}' marked as complete.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")


def remove_task(tasks):
    try:
        task_id = int(input("Enter the task ID to remove: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print(f"Task '{task['task']}' removed.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
