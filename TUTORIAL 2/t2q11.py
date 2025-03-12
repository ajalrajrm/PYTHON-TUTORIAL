def dec_to_bin(n):
    b_num = ""
    while n > 0:
        b_num = str(n % 2) + b_num
        n //= 2
    return b_num if b_num else "0"

n = int(input("Enter a decimal number: "))
print("Binary:", dec_to_bin(n))
