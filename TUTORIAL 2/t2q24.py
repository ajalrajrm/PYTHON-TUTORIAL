n = int(input("Enter number of elements: "))
nums = []
seen = set()

for _ in range(n):
    num = int(input("Enter number: "))
    if num not in seen:
        seen.add(num)
        nums.append(num)

print("List after removing duplicates:", nums)
