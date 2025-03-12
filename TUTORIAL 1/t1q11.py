n = int(input("Enter a positive integer: "))
even_cubes_sum = sum(i**3 for i in range(2, n+1, 2))

print(f"The sum of the cubes of even numbers is: {even_cubes_sum}")
