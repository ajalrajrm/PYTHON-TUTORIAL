n = int(input("Enter the total number of elements: "))
even_sum = 0

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    if num % 2 == 0:
        even_sum += num

print(f"The sum of even numbers is: {even_sum}")
