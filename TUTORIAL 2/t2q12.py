b = input("Enter a binary number: ")
dec_num = 0

for digit in b:
    dec_num = dec_num * 2 + int(digit)

print("Decimal:", dec_num)
