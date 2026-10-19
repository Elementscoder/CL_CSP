def fibonacci_sequence(n):
    # Generate the Fibonacci sequence
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

while True:
    try:
        # Ask the user for input
        num = int(input("Enter the number of Fibonacci numbers to print (between 1 and 20): "))
        if 1 <= num <= 20:
            # Generate the Fibonacci sequence
            fib_sequence = fibonacci_sequence(num)
            # Print each number with its number of digits
            print("Fibonacci sequence with number of digits:")
            print(" ".join(f"{x}({len(str(x))})" for x in fib_sequence))
            # Automatically restart the loop
            print("\nRestarting...\n")
        else:
            print("Please enter a number between 1 and 20.")
    except ValueError:
        print("Invalid input! Please enter a positive integer between 1 and 20.")