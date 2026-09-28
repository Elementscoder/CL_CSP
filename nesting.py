# CL, Nesting Notes

csp = ["Remy", "Alex", "Gabe", "Bliss", "Elsie", "Ivan", "Caydon", "Kaylee", "Levi", "Masen", "William", "Carrera", "Jocab", "Selena", "Ainsley", "Kristian"]
if len(csp) < 0:
    for student in csp:
        print(f"Checking in {student}")
else:
    print("There is no one in this class.")

while True:
    username = input("What is your username: ").strip()
    password = input("What is your password: ").strip()

    if username == "LaRose4" and password == "password":
        print("Welcome to the program!")
        break
    else:
        print("Those credentials were incorrect.")