# Cl, Loops Notes
import random
# code that will repeat over and over again
count = 1

while count <=10:
    print(count)
    count += 1

goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!")

siblings = ["Macie", "Atalie", "Connor", "Chase", "Coda", "Jordon", "Kellie", "Landon", "Chelsey", "Kaleb", "Marilyn", "Jared", "Sadie"]
niblings = ["Bradley", "Lenny", "Dane", "Lily", "Lola", "Milo", "Blake", "Athony", "Lakoa", "Maggie"]

print(siblings[2])
print(siblings)
# add to the list
item = input("What needs to be added to the list:\n")
siblings.append("LeBaron")
siblings.insert(1,"Caydon")
# remove from list
print(siblings)
print(siblings.pop(1))
print(siblings)
siblings.pop(1)

# for loops
for number in range(1,11,2):
    print(number)

for sibling in siblings:
    print(sibling + "LeBaron")