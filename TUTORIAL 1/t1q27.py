import math

a, b, c = map(float, input("Enter the coefficients a, b, and c: ").split())

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1:.2f}, {root2:.2f}")
else:
    print("No real roots")
