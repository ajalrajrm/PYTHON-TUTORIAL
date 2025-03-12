num = int(input("Enter a number: "))
power = len(str(num))
armstrong_sum = sum(int(digit) ** power for digit in str(num))

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
