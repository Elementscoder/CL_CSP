import random

print("I'm thinking of a integer between 1 and 100. You have 6 tries to guess it!")
number = random.randint(1,100)
guesses = 1

while guesses <=6:
    while True:
        try:
            guess = int(input(f"Guess #{guesses}:\n"))
            break
        except:
            print("That isn't an integer.")

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        break
    guesses += 1
if guesses <= 6:
    print(f"Congratulations! You guessed it {guesses} tries, Good Job!")
else:
    print(f"You're out of guesses! The number was {number}.")