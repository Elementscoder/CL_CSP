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
        print("""______
                 |    |
                 |
                 |
                 |
                 |_______""")
    elif wrong_guesses == 1:
        print("""______
                 |    |
                 |    O
                 |
                 |
                 |_______""")
    elif wrong_guesses == 2:
        print("""______
                 |    |
                 |    O
                 |    |
                 |
                 |_______""")
    elif wrong_guesses == 3:
        print("""______
                 |    |
                 |    O
                 |   /|
                 |
                 |_______""")
    elif wrong_guesses == 4:
        print("""______
                 |    |
                 |    O
                 |   /|\\
                 |
                 |_______""")
    elif wrong_guesses == 5:
        print("""______
                 |    |
                 |    O
                 |   /|\\
                 |   /
                 |_______""")
    else:
        if wrong_guesses == 6:
            print("""______
                     |    |
                     |    O
                     |   /|\\
                     |   / \\
                     |_______""")
    return hangman

while True:
    hangman(wrong_guesses)
    guess = input(f"Enter guess #{guesses} letter guess:\n")