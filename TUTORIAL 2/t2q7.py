s = input("Enter a string: ")

uppercase_string = "".join([ch.upper() if 'a' <= ch <= 'z' else ch for ch in s])

print("Uppercase string:", uppercase_string)
