n = int(input("Enter the number of values: "))
even_count = odd_count = 0

for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Count of even numbers: {even_count}, Count of odd numbers: {odd_count}")
