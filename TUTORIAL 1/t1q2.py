import math

r = float(input("Enter the circle's radius: "))
circle_area = math.pi * r ** 2
circle_perimeter = 2 * math.pi * r

print(f"Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")