# Set

# set is unordered collection of unique elements, no duplicates
my_set = {1, 2, 3, 4, 5, 5}

print(my_set)

my_set.add(100)

print(my_set)

print(1 in my_set)

print(list(my_set))

new_set = my_set.copy()

print(new_set)
new_set.clear()
print(new_set)


################################ SETS METHODS ##########################################

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}

# print(set1.difference(set2))
# print(set1.discard(5))
# print(set1)

# set1.difference_update(set2)

# print(set1)

# print(set1.intersection(set2)) # or print(set1 & set2)

# print(set1.isdisjoint(set2))

# print(set1.union(set2))  # or print( set1 | set2)

print(set1.issubset(set2))
print(set1.issuperset(set2))
