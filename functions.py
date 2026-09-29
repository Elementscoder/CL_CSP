# CL, Function Note

#round()
#len()
#print()
def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"What is your monthly {money}:\n"))
            return temp
        except:
            print("That is not a number")

income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
transportation = stupid_proof("transportation")
groceries = stupid_proof("groceries")
save = round(income*.1, 2)

# functions go second
def calc_percent(bill, income):
    return round(bill/income*100)

print(f"Your rent is ${rent} which is {calc_percent(rent, income)}% of your income")
print(f"Your utilities is ${utilities} which is {calc_percent(utilities, income)}% of your income")
print(f"Your transportation is ${transportation} which is {calc_percent(transportation, income)}% of your income")
print(f"Your groceries is ${groceries} which is {calc_percent(groceries, income)}% of your income")
print(f"You should save ${save} which is 10% of your income")
print(f"That means you saved {income-rent-utilities-transportation-groceries-save} left to spend.")