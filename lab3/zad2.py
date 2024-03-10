import random

list1 = [random.randint(1, 100) for x in range(10)]
list2 = [x for x in list1 if x % 2 == 0]

print(list1)
print(list2)