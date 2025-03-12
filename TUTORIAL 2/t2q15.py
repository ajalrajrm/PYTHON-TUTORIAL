def factors(n):
    print("Factors:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()  # Newline for better formatting

while True:
    print("\nMenu:")
    print("1. Check Even/Odd")
    print("2. Check Positive/Negative/Zero")
    print("3. Generate Factors")
    print("4. Exit")

    try:
        ch = int(input("Enter choice: "))
        if ch == 1:
            num = int(input("Enter number: "))
            print("Even" if num % 2 == 0 else "Odd")
        elif ch == 2:
            num = int(input("Enter number: "))
            print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
        elif ch == 3:
            num = int(input("Enter number: "))
            factors(num)
        elif ch == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
