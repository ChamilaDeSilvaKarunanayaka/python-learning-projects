def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


tasks = []

while True:
    print("\nTo-Do List Manager")
    print("------------------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_task(tasks)
