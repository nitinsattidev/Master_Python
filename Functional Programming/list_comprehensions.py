# Also call as  list/set/dictionary comprehensions

my_list1 = [char for char in "hello"]

print(my_list1)

my_list2 = [num * 2 for num in range(1, 100)]

print(my_list2)

my_list3 = [num**2 for num in range(1, 100) if num % 2 == 0]

print(my_list3)
