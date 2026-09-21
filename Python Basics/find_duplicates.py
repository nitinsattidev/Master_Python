# Exercise: CHeck for duplicates in a list

some_list = ["a", "b", "c", "d", "e", "d", "m", "n", "a", "n"]


duplicates = []

for element in some_list:
    if some_list.count(element) > 1 and element not in duplicates:
        duplicates.append(element)

print(duplicates)
