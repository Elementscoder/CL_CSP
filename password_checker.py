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
    points = points+1
else:
    points = points+0
if upcase == True:
    points = points+1
else:
    points = points+0
if lowcase == True:
    points = points+1
else:
    points = points+0
if number == True:
    points = points+1
else:
    points = points+0
if symbol == True:
    points = points+1
else:
    points = points+0
while True:
    if points == 5:
        print("Your password strength is strong.")
    elif points == 3 or points == 4:
        print("Your password strength is medium.")
    else:
        print("Your password strength is weak.")
    break
if length == False:
    need_8 = "at least eight characters"
if upcase == False:
    need_up = "an uppercase letter"
if lowcase == False:
    need_low = "an lowercase letter"
if number == False:
    need_number = "a number"
if symbol == False:
    need_symbol = "a symbol"

print("to make your password strong you need "+need_8+", "+need_up+", "+need_low+", "+need_number+", and"+need_symbol+".")