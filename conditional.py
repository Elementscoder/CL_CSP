# CL, Conditionals Notes

military_time = int(input("Tell me the military time without a space and colon:\n"))

if military_time >= 1200 and military_time < 1700:
    print("It's the afternoon")
elif military_time < 1200:
    print("It's morning")
elif military_time >= 1700 and military_time < 2200:
    print("It's the evening")
else:
    print("It's the night")

# nesting conditionals
day = "Saturday"
time = 900

if time > 900 and time < 1600:
    if day != "Saturday" or day != "Sunday":
        print("You should be at school!")
    else:
        if time > 1200:
            print("Good Afternoon")
        else:
            print("Good Morning")
else:
    print("You are not required to be at school")