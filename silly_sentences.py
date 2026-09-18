# CL, 7, Silly Sentences
while True:
  verb = input('Tell me a verb ending in "ing":\n').strip().capitalize()
  if verb.isnumeric():
    print("That is a number")
  elif " " in verb:
    print("Only one verb")
  else:
    break
while True:
  place = input('Tell me a place:\n').strip().capitalize()
  if place.isnumeric():
    print("That is a number")
  elif " " in place:
    print("Only one place")
  else:
    break
while True:
  color = input('Tell me a color:\n').strip().capitalize()
  if color.isnumeric():
    print("That is a number")
  elif " " in color:
    print("Only one color")
  else:
    break
while True:
  vehicle = input('Tell me a transportation vehicle:\n').strip().capitalize()
  if vehicle.isnumeric():
    print("That is a number")
  elif " " in vehicle:
    print("Only one vehicle")
  else:
    break
while True:
  emotion = input('Tell me an emotion:\n').strip().capitalize()
  if emotion.isnumeric():
    print("That is a number")
  elif " " in emotion:
    print("Only one emotion")
  else:
    break
while True:
  animal = input('Tell me a animal:\n').strip().capitalize()
  if animal.isnumeric():
    print("That is a number")
  elif " " in animal:
    print("Only one animal")
  else:
    break

print(f"I was going to be late for my {verb} job in {place} when my {color} {vehicle} got destroyed by a {emotion} {animal}")
