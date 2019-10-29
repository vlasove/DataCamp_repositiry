def func_name():
    return 21


print(type(func_name()))
print(type(func_name))


def another_func(*args):
    for i in args:
        print(i)


another_func(1, 2, 4, 124353432, 3, 543, 6)


def name(name):
    return name


print(name(2))
