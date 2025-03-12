low, high = map(int, input("Enter the lower and upper limits: ").split())
sum_of_odds = sum(num for num in range(low, high + 1) if num % 2 != 0)

print(f"Sum of odd numbers in the range: {sum_of_odds}")
