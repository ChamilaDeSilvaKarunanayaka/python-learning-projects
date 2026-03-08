class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


accounts = {}

while True:
    print("\nBank Menu")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial deposit: "))

        account = BankAccount(name, initial_balance)
        accounts[name] = account

        print("Account created successfully!")

    elif choice == "2":
        name = input("Enter account holder name: ")

        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        name = input("Enter account holder name: ")

        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account holder name: ")

        if name in accounts:
            accounts[name].check_balance()
        else:
            print("Account not found.")

    elif choice == "5":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice. Try again.")