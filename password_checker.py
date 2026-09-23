# CL, Password Strength Checker

password = input("Give me a password:\n").strip()
length = False
upcase = False
lowcase = False
number = False
symbol = False
points = 0

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
    point = point+1
else:
    point = point+0
if upcase == True:
    point = point+1
else:
    point = point+0
if lowcase == True:
    point = point+1
else:
    point = point+0
if number == True:
    point = point+1
else:
    point = point+0
if symbol == True:
    point = point+1
else:
    point = point+0
while True:
    if point == 5:
        print(f"Your password strength is strong")
    elif point == 3 or 4:
        print(f"Your password strength is medium")
    else:
        print(f"Your password strength is weak")
break

