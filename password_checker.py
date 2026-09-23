# CL, Password Strength Checker

password = input("Give me a password:\n").strip()
length = False
upcase = False
lowcase = False
number = False
symbol = False
points = 0
feedback = "To make it strong add: "

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

if length == True:
    points = points+1
else:
    feedback = feedback+"at least eight characters, "
if upcase == True:
    points = points+1
else:
    feedback = feedback+"an uppercased letter, "
if lowcase == True:
    points = points+1
else:
    feedback = feedback+"an lowercased letter, "
if number == True:
    points = points+1
else:
    feedback = feedback+"a number, "
if symbol == True:
        points = points+1
else:
    feedback = feedback+"a symbol."
if length == True and upcase == True and lowcase == True and number == True and symbol == True:
    feedback = feedback+"nothing"
else:
    feedback = feedback+""

while True:
    if points == 5:
        print("Your password strength is strong.")
    elif points == 3 or points == 4:
        print("Your password strength is medium.")
    else:
        print("Your password strength is weak.")
    break

print(feedback)