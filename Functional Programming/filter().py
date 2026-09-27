def only_odd(item):
    return item % 2 != 0


print(filter(only_odd, [1, 2, 5, 7, 8, 10, 4, 3]))
print(list(filter(only_odd, [1, 2, 5, 7, 8, 10, 4, 3])))
