s = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_string = "".join([char for char in s if char not in vowels])

print("String after removing vowels:", new_string)
