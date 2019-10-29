

while True:
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    if x1 == -1 and y1 == -1 and x2 == -1 and y2 == -1:
        break

    if (abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(y1-y2) == 2 and abs(x1-x2)==1):
        print("YES")
    else:
        print("NO")
