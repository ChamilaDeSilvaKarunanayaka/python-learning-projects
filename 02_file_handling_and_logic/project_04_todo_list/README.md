# To-Do List Manager (File Based)

This is a simple Python command-line To-Do List application.
It allows users to add tasks, view tasks, and save tasks permanently in a file.

## Features
- Add new tasks
- View all tasks with numbering
- Save tasks to a file (tasks.txt)
- Load tasks automatically when the program starts
- Menu-driven system
- Handles file errors safely

## Concepts Used
- Functions (def)
- while loop
- Lists
- for loop
- enumerate()
- File handling (open, read, write)
- Exception handling (try / except)
- break statement

## How It Works
- Tasks are stored in a list.
- When a task is added, it is saved to a file named `tasks.txt`.
- When the program starts, it reads `tasks.txt` and loads previous tasks.
- The program runs continuously until the user selects Exit.

## How to Run
1. Open terminal in this project folder.
2. Run:

   python main.py

## Example Menu

To-Do List Manager
------------------
1. Add task
2. View tasks
3. Exit

## Notes
- Tasks are saved in a file called `tasks.txt`.
- If the file does not exist, the program creates it automatically.
- Tasks remain saved even after closing the program.