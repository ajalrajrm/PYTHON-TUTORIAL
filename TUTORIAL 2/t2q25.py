n = int(input("Enter number of elements: "))
ints, floats, strs = [], [], []

for _ in range(n):
    val = input("Enter value: ")
    
    # Check if integer
    if val.lstrip('-').isdigit():
        ints.append(int(val))
    
    # Check if float (handling negatives correctly)
    elif val.count('.') == 1 and val.replace('.', '').lstrip('-').isdigit():
        floats.append(float(val))
    
    # Otherwise, it's a string
    else:
        strs.append(val)

print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strs)
