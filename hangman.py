# CL, Hangman Game

import random

word = ""
guesses = 1
wrong_guesses = 0

with open('hangman.txt', "r") as file:
    content = file.read()
    words = content.split(",")
    word = random.choice(words)

def hangman(wrong_guesses):
    if wrong_guesses == 0:
        print("""
                 ______
                 |    |
                 |
                 |
                 |
                 |_______""")
    elif wrong_guesses == 1:
        print("""
                 ______
                 |    |
                 |    O
                 |
                 |
                 |_______""")
    elif wrong_guesses == 2:
        print("""
                 ______
                 |    |
                 |    O
                 |    |
                 |
                 |_______""")
    elif wrong_guesses == 3:
        print("""
                 ______
                 |    |
                 |    O
                 |   /|
                 |
                 |_______""")
    elif wrong_guesses == 4:
        print("""
                 ______
                 |    |
                 |    O
                 |   /|\\
                 |
                 |_______""")
    elif wrong_guesses == 5:
        print("""
                 ______
                 |    |
                 |    O
                 |   /|\\
                 |   /
                 |_______""")
    else:
        if wrong_guesses == 6:
            print("""
                     ______
                     |    |
                     |    O
                     |   /|\\
                     |   / \\
                     |_______""")
    return hangman

def display_word(word):
    letter_word = ""
    while True:
        length = len(word)
        if length == 0:
            break
        else:
            if length != 0:
                letter_word = letter_word + "_"
                length -= 1
                continue  
    for letter in word:
        if guess == letter:
            letter_word.replace("_", letter)
        else:
            wrong_guesses = wrong_guesses + 1
        return letter_word

while True:
    hangman(wrong_guesses)
    print(display_word(word))

    while True:
        guess = input(f"Enter guess #{guesses} letter guess:\n").lower()
        if guess.isalpha():
            break
        else:
            if len(guess) > 1:
                print("Please type only one character.")
                continue
            else:
                continue