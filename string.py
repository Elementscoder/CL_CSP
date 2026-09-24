# CL, String Notes

last_name = "Caydon" 
# surround with quotes
first_name = "LeBaron" 
# surround with quotes

# concatenation => add two string together
name = first_name + " " + last_name 
# puts two strings next to each other in the same string

# excape character lets the program ignore the next character in the string
print(f'{name} told the class "You can\'t drive my car."') 
# f-string = formated string, 1. easy in sort variable, easier to specify having it print for the user

user = input("Please tell me your name:\n").strip().title()

print(f"New user recognized\nWelcome {user}")

sentence = "The quick brown fox jumped over the lazy dog."
print(f"The sentence is {len(sentence)} characters long.")
print(sentence)
print(sentence.replace("dog", "cat"))