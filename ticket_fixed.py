# CL, Fixed Ticket


try:
    age = int(input("Enter your age: "))
    matinee = input("Is this a matinee? (yes/no): ").lower()

    if age < 5:
        price = 0.00
    elif age <= 12:
        price = 8.00
    elif age < 65:
        price = 12.00
    else:
        price = 9.00

    if matinee == "yes" and price != 0:
        price -= 3

    print(f"Ticket price: ${price:.2f}")
except:
    print("Invalid age")