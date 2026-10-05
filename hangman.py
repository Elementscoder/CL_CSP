# CL, Hangman Game

import random

word = ""
guesses = 1
wrong_guesses = 0
guessed = []

with open('hangman_win_loss.txt', "r") as file:
    content = file.read()
    scores = content.split(",")
    wins = int(scores[0])
    loses = int(scores[1])

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

    while True:
        guess = input(f"Enter guess:\n").lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Please type only one alpabetical character.")
            continue
    
    guessed.append(guess)
    if guess not in word:
            wrong_guesses += 1
    if display_word(word, guessed) == word and wrong_guesses <= 6:
        print("You won!")
        wins += 1
        play = input("Do you want to play again:\n").lower()
        if play == "yes":
            wrong_guesses = 0
            word = random.choice(words)
        else:
            print(f"Okay you have {wins} wins and {loses} loses.\nData has been reset.")
            wins = 0
            loses = 0
            wrong_guesses = 7
    else:
        if wrong_guesses > 6:
            print("You lose!")
            print(f"The word was {word}")
            loses += 1
            play = input("Do you want to play again:\n").lower()
            if play == "yes":
                wrong_guesses = 0
                word = random.choice(words)
            else:
                print(f"Okay you have {wins} wins and {loses} loses.\nData has been reset.")
                wins = 0
                loses = 0
                wrong_guesses = 7
        else:
            continue