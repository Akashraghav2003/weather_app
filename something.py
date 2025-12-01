# guess_game.py

import random

print("Welcome to the Number Guessing Game!")
secret = random.randint(1, 50)

attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
