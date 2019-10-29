#fname = "input.txt"

# with open(fname, "r") as files:
#    lines = files.read()
#    for line in lines:
#        print(line)

name = "Hello world"
name_list = list(name)
dict_counter = {}
for letter in name.lower():
    dict_counter[letter] = dict_counter.get(letter, 0) + 1

print(dict_counter)
