import random

secret_number = random.randint(1, 10)
 # For testing purposes; remove or comment out in production
guess = 0
attempts = 0

while guess != secret_number:
 guess = int(input("Guess a number between 1 and 10: "))
 attempts += 1

 if guess == secret_number:
    print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
 else:
    print("❌ Wrong guess. Try again!")
