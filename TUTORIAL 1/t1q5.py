import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The equation has two distinct real roots: {root1:.2f} and {root2:.2f}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The equation has one repeated real root: {root:.2f}")
else:
    print("The equation has no real roots.")
