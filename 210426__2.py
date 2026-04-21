import random

guess = int(input("Guess a number between 0 and 100: "))
number = random.randint(0, 100)

while guess != number:
    # keep guessing until the guess is correct
    if guess > number:
        print(f"{guess} is too high.")
    elif guess < number:
        print(f"{guess} is too low.")
    guess = int(input("Guess again: "))
print("Correct!")