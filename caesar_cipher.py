# CL, Caesar Cipher

crypting = input("Would you like to (E)ncrypt or (D)ecrypt a message:\n")
message = input("Enter your message:\n")
shift = int(input("Enter your shift amount:\n"))

def encrypt(message, shift):
    for letter in message:
        if letter.isalpha:
            letter = ord(letter) + shift
            letter = chr(letter)
        print(letter)

encrypt(message, shift)