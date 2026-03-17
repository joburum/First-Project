tasks = []  # each item: {"name": str, "done": bool}

def print_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print()
    for i, task in enumerate(tasks, 1):
        status = "x" if task["done"] else " "
        print(f"  {i}. [{status}] {task['name']}")

def pick_task(prompt):
    view_tasks()
    if not tasks:
        return None
    try:
        n = int(input(prompt))
        if 1 <= n <= len(tasks):
            return n - 1
        print("Invalid number.")
    except ValueError:
        print("Please enter a number.")
    return None

while True:
    print_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Task name: ").strip()
        if name:
            tasks.append({"name": name, "done": False})
            print(f"Added: {name}")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        idx = pick_task("Mark which task as done? ")
        if idx is not None:
            tasks[idx]["done"] = True
            print(f"Marked done: {tasks[idx]['name']}")
    elif choice == "4":
        idx = pick_task("Delete which task? ")
        if idx is not None:
            print(f"Deleted: {tasks[idx]['name']}")
            tasks.pop(idx)
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Invalid option, try again.")
