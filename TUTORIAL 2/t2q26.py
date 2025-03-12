def is_prime(n):
    if n < 2:  # 0 and 1 are neither prime nor composite
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter number of elements: "))
nums = [int(input("Enter number: ")) for _ in range(n)]

primes = [num for num in nums if is_prime(num)]
composites = [num for num in nums if num > 1 and not is_prime(num)]
neither = [num for num in nums if num <= 1]  # Handling 0 and 1 separately

print("Primes:", primes)
print("Composites:", composites)
if neither:
    print("Neither prime nor composite:", neither)
