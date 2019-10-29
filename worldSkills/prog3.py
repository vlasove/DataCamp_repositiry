#С консоли вводится слово. Если это слово "мяу" - то на выходе программа
#должна выдать "кот", иначе -- "пёс"



#if input() == "мяу":
#    print("кот")
#else:
#    print("пёс")




x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

if (abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(y1-y2) == 2 and abs(x1-x2)==1):
    print("YES")
else:
    print("NO")