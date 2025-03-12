from collections import Counter

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]

count = Counter(nums)
mode = [k for k, v in count.items() if v == max(count.values())]  # Handles multiple modes

print("Mode:", mode if len(mode) > 1 else mode[0])
