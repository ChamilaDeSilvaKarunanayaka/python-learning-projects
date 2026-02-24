import random
import string


# Step 1: Get valid password length
while True:
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


# Step 2: Ask user which character types to include
use_letters = input("Include letters? (y/n): ").lower()
use_digits = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if use_letters == "y":
    characters += string.ascii_letters

if use_digits == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation


# Step 3: Check if at least one type selected
if characters == "":
    print("You must select at least one character type.")
    exit()


# Step 4: Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)