n = int(input("Enter the range: "))

for i in range(1, n + 1):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} × {j} = {i * j}")
    print()
