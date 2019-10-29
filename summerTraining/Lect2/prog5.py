# Collections
# Dictionary
# 4

my_dict = {0: 1, True: 2, None: 4, (1, 2, 3, 4): 1234}
my_dict["one"] = 2


print(my_dict[True])
print(my_dict)


for k, v in my_dict.items():
    print(k, v)
