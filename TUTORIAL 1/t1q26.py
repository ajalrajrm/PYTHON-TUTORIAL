x1, y1 = map(int, input("Enter the first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter the second point (x2 y2): ").split())

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"Distance between the points: {distance:.2f}")
