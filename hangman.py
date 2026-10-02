# CL, Hangman Game

import random
word = ""
wrong_guesses = 0

with open('hangman.txt', "r") as file:
    content = file.read()
    words = content.split(",")
    word = random.choice(words)

