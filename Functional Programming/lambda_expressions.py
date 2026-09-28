# lambda expressions
from functools import reduce

my_list = [1, 2, 3, 4]

print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 10))

list1 = [5, 4, 3]
new_list = list(map(lambda item: item * item, list1))
print(new_list)


# List Sorting

a = [(0, 2), (9, 9), (10, -1), (4, 3)]
b = list(map(lambda item: item[::-1], a))
b.sort()
c = list(map(lambda item: item[::-1], b))
print(c)


# the above one is lengthy and not one liner lambda, better way is below

d = [(0, 2), (9, 9), (10, -1), (4, 3)]
d.sort(key=lambda item: item[1])
print(d)
