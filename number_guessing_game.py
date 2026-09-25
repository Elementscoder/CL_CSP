import random

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")
number = random.randint(1,100)

while True:
    guess = int(input("Guess #1:\n"))
    if guess == number:
        print("Correct! You guessed it in ")
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
        break
