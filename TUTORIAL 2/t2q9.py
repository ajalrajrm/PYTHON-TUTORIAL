s = input("Enter a string: ")
n = len(s)
mid = n // 2

first_half_reversed = s[:mid][::-1]
second_half_reversed = s[mid:][::-1]

modified_string = first_half_reversed + second_half_reversed

print("Modified string:", modified_string)
