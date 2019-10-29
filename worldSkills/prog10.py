#Написать функцию расчета квадратного корня числа n


def mySqrt(a):
    xn = 9329128894238
    for i in range(0,100):
        xn = 1/2*(xn + a/xn)
        print(xn)
    return xn

print(mySqrt(9))