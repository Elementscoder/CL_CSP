# CL, Number Information

for number in range(1,21):
    if number%2:
        if number%5:
            print(number, "is odd and not divisible by 5")
        else:
            print(number, "is odd and divisible by 5")
    else:
        if number%5:
            print(number, "is even and not divisible by 5")
        else:
            print(number, "is even and divisible by 5")