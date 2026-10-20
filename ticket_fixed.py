# CL, Fixed Ticket

while True:
    age = int(input("Enter your age: "))
    matinee = input("Is this a matinee? (yes/no): ").lower()

    if age.isnumeric():
        if age < 5:
            price = 0
            break
        elif age < 12:
            price = 8
            break
        elif age < 65:
            price = 12
            break
        else:
            price = 9
            break
    else:
        print("Please enter a valid age.")
        continue

if matinee == "yes" and price != 0:
    price = price - 3

print(f"Ticket price: ${price}")