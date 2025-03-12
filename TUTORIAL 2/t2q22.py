n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]
nums.sort()

m = n // 2
median = nums[m] if n % 2 == 1 else (nums[m - 1] + nums[m]) / 2
print("Median:", median)
