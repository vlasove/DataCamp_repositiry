temp = input()
nums = temp.split()
n = int(nums[0])
k = int(nums[1])

c = int((k - k%n )/n)
print(c)
