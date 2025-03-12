x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x > 0 and y > 0:
    print("The point lies in Quadrant 1.")
elif x < 0 and y > 0:
    print("The point lies in Quadrant 2.")
elif x < 0 and y < 0:
    print("The point lies in Quadrant 3.")
elif x > 0 and y < 0:
    print("The point lies in Quadrant 4.")
elif x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
else:
    print("The point lies on the X-axis.")
