import math

def factorial(n):
    """Returns the factorial of n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

sin_x = sum(((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))

print(f"sin({x}) ≈ {sin_x}")
print(f"Actual sin({x}) = {math.sin(x)} (Using math.sin)")
