print("Simple Calculator")
print("-----------------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

choice = int(input("Enter your choice (1-5):"))
print("You selected:", choice)

if choice == 1:
    print("You chose Addition")
elif choice == 2:
    print("You chose Subtraction")
elif choice == 3:
    print("You chose Multiplication")
elif choice == 4:
    print("You chose Division")
elif choice == 5:
    print("Exiting calculator...")
else:
    print("Invalid choice")