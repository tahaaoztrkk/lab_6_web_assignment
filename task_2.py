# Task 2: Guess the Secret Number

import random

secret = random.randint(1, 20)
attempts = 5

print("I have chosen a number between 1 and 20. You have 5 attempts!")

for i in range(attempts):
    guess = int(input("Enter your guess: "))
    
    if guess == secret:
        print("Congratulations! You won the reward!")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

if guess != secret:
    print(f"Sorry, you lost! The number was {secret}.")
