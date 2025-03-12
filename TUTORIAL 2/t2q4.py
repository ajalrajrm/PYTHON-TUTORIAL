s = input("Enter a string: ")

if " " in s:
    modified_string = s.replace(" ", "*")
else:
    modified_string = "$" + s + "$"

print("Modified string:", modified_string)
