

start = int(input())
end = int(input())

for i in range(start, end+1):
    if i % 2 == 0:
        print(i**2)
    else:
        print(i**3)


#Вывести в поток i**2 если i - четное число
#Вывести в поток i**3 если i - нечетное число

#0
#9

#0, 1, 4, 27, 16, 125, 36, .....
