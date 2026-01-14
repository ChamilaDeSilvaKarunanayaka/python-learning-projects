import random

secret_number = random.randint(1, 10)

print(secret_number) # For testing purposes; remove or comment out in production

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🎉 Correct! You guessed the number.")
else:
    print("❌ Wrong guess. Try again!")
