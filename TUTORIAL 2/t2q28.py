A = set(map(int, input("Enter space-separated elements of set A: ").split()))
B = set(map(int, input("Enter space-separated elements of set B: ").split()))

print("Union:", sorted(A | B))
print("Intersection:", sorted(A & B))
print("Difference (A - B):", sorted(A - B))
print("Difference (B - A):", sorted(B - A))
print("Symmetric Difference:", sorted(A ^ B))
