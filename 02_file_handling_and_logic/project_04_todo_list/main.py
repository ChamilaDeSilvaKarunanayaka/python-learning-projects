def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

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

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")    
