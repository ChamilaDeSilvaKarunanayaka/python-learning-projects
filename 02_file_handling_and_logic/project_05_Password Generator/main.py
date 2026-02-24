import random
import string

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Password length should be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)