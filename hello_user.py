# CL, Hello User

while True:
    name = input("What is your name: ").capitalize().strip()
    if name.isnumeric():
        print("Sorry that is a number")
    elif " " in name:
        print("Only your first name")
    else:
        break

print(f"Hello {name}, it is nice to meet you")