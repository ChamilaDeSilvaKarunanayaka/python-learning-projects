students = {}

while True:
    print("\nStudent Marks Manager")
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

    elif choice == 3:
        if not students:
            print("No students to calculate average.")
        else:
            total = 0
            for mark in students.values():
                total += mark
            average = total / len(students)
            print(f"Average mark: {average}")

    elif choice == 4:
        if not students:
            print("No students found.")
        else:
            highest_name = max(students, key=students.get)
            highest_mark = students[highest_name]
            print(f"Highest mark: {highest_name} ({highest_mark})")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
