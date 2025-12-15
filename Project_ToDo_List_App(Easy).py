def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return

    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

tasks = load_tasks()

while True:
    print("\n1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save & Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
