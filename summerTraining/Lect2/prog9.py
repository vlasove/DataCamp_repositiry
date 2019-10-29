class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def summator(self):
        return self.arg1+self.arg2


my_ex = MyClass(2, 3)
print(my_ex.arg1, my_ex.arg2)
print(my_ex.summator())
