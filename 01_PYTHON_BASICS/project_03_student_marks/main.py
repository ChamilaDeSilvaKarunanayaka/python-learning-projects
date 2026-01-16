students = {}

print("Student Marks Manager")
print("---------------------")
print("1. Add student mark")
print("2. Display all students")
print("3. Calculate average")
print("4. Show highest mark")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    name = input("Enter student name: ")
    mark = float(input("Enter student mark: "))
    students[name] = mark
    print("Student added successfully!")

elif choice == 2:
    if not students:
        print("No students found.")
    else:
        print("Student Marks:")
        for name, mark in students.items():
            print(f"{name} : {mark}")