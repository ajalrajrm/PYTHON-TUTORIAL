txt = input("Enter a string: ")

if txt == txt[::-1]:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
