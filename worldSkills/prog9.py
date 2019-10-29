#Функция!!!!!!
#isSimple(n)
#Функция проверяет, является ли число n - простым. 1 - не простое число

def isSimple(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count += 1
    
    if count == 2:
        return True
    return False


for i in range(0,50):
    if isSimple(i):
        print(i)