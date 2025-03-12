s = input("Enter string: ")
word = input("Enter word to remove: ")
print("Modified string:", s.replace(f"{word} ", "").replace(f" {word}", "").replace(word, ""))
