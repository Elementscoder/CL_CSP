# CL, Caesar Cipher

def stupid_proof(question):
    while True:
        inputs = input(question)
        if inputs.isnumeric():
            print("Sorry that is a number.")
        else:
            return inputs

message = stupid_proof("Enter your message:\n")

while True:
    try:
        shift = int(input("Enter your shift:\n"))
        break
    except:
        print("That isn't a number.")

while True:
    crypt = stupid_proof("Would you like to (E)ncrypt or (D)ecrypt a message:\n")
    if crypt == "E":
        if shift < 0:
            shift = 0-shift
    elif crypt == "D":
        shift = 0-shift
    else:
        print('You need to type "E" or "D" for (E)ncrypt and (D)ecrypt')
    break

def encrypt(message, shift):
    word = ""
    for letter in message:
        if letter.isalpha():
            uppercase = letter.isupper()
            letter = ord(letter) + shift
            if not uppercase and letter > 122 and shift > 0:
                letter = letter - 26
            elif not uppercase and letter < 97 and shift <0:
                letter = letter + 26
            elif uppercase and letter > 90 and shift > 0:
                letter = letter - 26
            elif uppercase and letter < 65 and shift < 0:
                letter = letter + 26
            letter = chr(letter)
            word = word+letter
    return word

print(encrypt(message, shift))