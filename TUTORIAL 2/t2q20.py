n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
even_sum = sum(num for num in nums if num % 2 == 0)
print("Sum of even numbers:", even_sum)
