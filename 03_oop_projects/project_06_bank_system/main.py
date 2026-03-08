class BankAccount:
    def __init__(self, owner, balance=0): # Constructor to initialize the bank account with an owner and an optional initial balance
        self.owner = owner # Set the owner of the bank account(object attribute)
        self.balance = balance # Set the initial balance of the bank account(object attribute)

    def deposit(self, amount): # Method to deposit money into the bank account(object method)
        self.balance += amount # Increase the balance by the deposited amount(object attribute)
        print(f"Deposited {amount}. New balance: {self.balance}") #

    def withdraw(self, amount): # Method to withdraw money from the bank account(object method)
        if amount > self.balance: # Check if the withdrawal amount is greater than the current balance
            print("Insufficient balance!")
        else:
            self.balance -= amount # Decrease the balance by the withdrawn amount(object attribute)
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self): # Method to check the current balance of the bank account(object method)
        print(f"Current balance: {self.balance}")
        
account1 = BankAccount("Dilshan", 1000) # Create an instance of the BankAccount class with the owner "Dilshan" and an initial balance of 1000

while True:
    print("\nBank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        account1.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        account1.withdraw(amount)
    elif choice == "3":
        account1.check_balance()
    elif choice == "4":
        print("Thank you for using our banking system!")
        break
    else:
        print("Invalid choice. Please try again.")
