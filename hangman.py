# CL, Hangman Game

import random

word = ""
guesses = 1
wrong_guesses = 0
guessed = []
win = 0
loses = 0

with open('hangman.txt', "r") as file:
    content = file.read()
    words = content.split(",")
    word = random.choice(words)

def hangman(wrong_guesses):
    if wrong_guesses == 0:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|
|
|
|_______""")
    elif wrong_guesses == 1:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|    O
|
|
|_______""")
    elif wrong_guesses == 2:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|    O
|    |
|
|_______""")
    elif wrong_guesses == 3:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|    O
|   /|
|
|_______""")
    elif wrong_guesses == 4:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|    O
|   /|\\
|
|_______""")
    elif wrong_guesses == 5:
        print(f"""______
|    |  wrong guesses: {wrong_guesses}
|    O
|   /|\\
|   /
|_______""")
    elif wrong_guesses == 6:
        print(f"""______
|    | wrong guesses: {wrong_guesses}
|    O
|   /|\\
|   / \\
|_______""")
    return hangman

def display_word(word, guessed):
    letter_word = ""
    for letter in word:
        if letter in guessed:
            letter_word = letter_word + letter
        else:
            letter_word = letter_word + "_"
    return letter_word

while True:
    hangman(wrong_guesses)
    print(display_word(word, guessed))
    guess = input(f"Enter guess #{guesses} letter guess:\n").lower()
    guessed = guessed + guess
    for letter in word:
        if letter != guess:
            wrong_guesses += 1
    if display_word == word and wrong_guesses <= 6:
        print("You won!")
        win += 1
        play = input("Do you want to play again:\n")
        if play == "yes" or "Yes":
            wrong_guesses = 0
            word = random.choice(words)
    else:
        print("You lose!")
        print(f"The word was {word}")
        loses += 1
