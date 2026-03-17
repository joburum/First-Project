tasks = []

while True:
    task = input("Enter a task (or 'done' to finish): ").strip()
    if task.lower() == "done":
        break
    if task:
        tasks.append(task)

print("\nYour tasks:")
for i, task in enumerate(tasks, 1):
    print(f"  {i}. {task}")
