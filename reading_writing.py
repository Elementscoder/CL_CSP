# CL, Reading and Writing to File

with open('practice.txt', "r+") as file:
    content = file.read()
    print(content)
    word = content.find("LeBaron")
    length = len("LeBaron")
    content += " Treyson!"
    print(content.upper())
    print(content[word:word+length])
    file.write(content)

with open('practice.txt', "a") as file:
    file.write("Another line")