# CL, Password Strength Checker

password = input("Give me a password:\n").strip()
length = False
upcase = False
lowcase = False
number = False
symbol = False

if len(password) >= 8:
    length = True
    print(f"Has at least eight characters: {length}")
else:
    print(f"Has at least eight characters: {length}")

for letter in password:
    if letter.isupper():
        upcase = True
    if letter.islower():
        lowcase = True
    if letter.isnumeric():
        number = True
    if letter in "!@#$%^&*":
        symbol = True

print(f"Has a uppercase letter: {upcase}")
print(f"Has a losercase letter: {lowcase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")