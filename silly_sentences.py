# CL, 7, Silly Sentences
while True:
  verb = input('Tell me a verb ending in "ing":\n').strip().lower()
  if verb.isnumeric():
    print("That is a number")
  elif " " in verb:
    print("Only one verb")
  else:
    break
while True:
  place = input('Tell me a place:\n').strip().title()
  if place.isnumeric():
    print("That is a number")
  else:
    break
while True:
  color = input('Tell me a color:\n').strip().lower()
  if color.isnumeric():
    print("That is a number")
  elif " " in color:
    print("Only one word colors")
  else:
    break
while True:
  vehicle = input('Tell me a transportation vehicle:\n').strip().lower()
  if vehicle.isnumeric():
    print("That is a number")
  else:
    break
while True:
  emotion = input('Tell me an emotion:\n').strip().lower()
  if emotion.isnumeric():
    print("That is a number")
  elif " " in emotion:
    print("Only one emotion")
  else:
    break
while True:
  animal = input('Tell me a animal:\n').strip().lower()
  if animal.isnumeric():
    print("That is a number")
  elif " " in animal:
    print("Only one animal")
  else:
    break

print("The bus was going in the wrong direction for my"+" "+verb+" "+"compitition in"+" "+place+" "+"and I couldn't drive myself because my"+" "+color+" "+vehicle+" "+"got destroyed by a"+" "+emotion+" "+animal+".")