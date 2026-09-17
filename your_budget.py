# CL, Your Budget

while True:
    try:
        income = int(input("What is your monthly income: $"))
        break
    except:
        print("That isn't an integer")
while True:
    try:
        rent = int(input("What is your monthly rent/mortgage: $"))
        break
    except:
        print("That isn't an integer")
while True:
    try:
        utility = int(input("What is your monthly utilities: $"))
        break
    except:
        print("That isn't an integer")
while True:
    try:
        grocery = int(input("What is your monthly groceries: $"))
        break
    except:
        print("That isn't an integer")
while True:
    try:
        transportation = int(input("What is your monthly transportation: $"))
        break
    except:
        print("That isn't a integer")

print(f"Your rent is ${rent:.2f} and that is {int(100*rent/income)}% of your income")
print(f"Your rent is ${utility:.2f} and that is {int(100*utility/income)}% of your income")
print(f"Your rent is ${grocery:.2f} and that is {int(100*grocery/income)}% of your income")
print(f"Your rent is ${transportation:.2f} and that is {int(100*transportation/income)}% of your income")
print(f"You have ${income-rent-utility-grocery-transportation:.2f} of spending money each month")