class BankAccount: # Define the BankAccount class
    def __init__(self, owner, balance=0): # Initialize the BankAccount class with owner and balance
        self.owner = owner # Set the owner of the account(object attribute)
        self.balance = balance # Set the balance of the account(object attribute)

    def deposit(self, amount): # Define the deposit method to add money to the account(object method    )
        self.balance += amount # Add the deposit amount to the current balance(object attribute)
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount): # Define the withdraw method to take money out of the account(object method)
        if amount > self.balance: # Check if the withdrawal amount is greater than the current balance(object attribute)    
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        
        
# Save accounts to file
def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for name, account in accounts.items():
            file.write(f"{name},{account.balance}\n")


# Load accounts from file
def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                name, balance = line.strip().split(",")
                accounts[name] = BankAccount(name, float(balance))
    except FileNotFoundError:
        pass
    return accounts


# Load saved accounts
accounts = load_accounts()


# Bank system menu
while True: # Start an infinite loop to display the bank menu and process user choices
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

        save_accounts(accounts)
        print("Account created successfully!")

    elif choice == "2":
        name = input("Enter account holder name: ")

        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[name].deposit(amount)
            save_accounts(accounts)
        else:
            print("Account not found.")

    elif choice == "3":
        name = input("Enter account holder name: ")

        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[name].withdraw(amount)
            save_accounts(accounts)
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