# SET Comprehension

my_list1 = {char for char in "hello"}

my_list2 = {num for num in range(1, 100)}

my_list3 = {num**2 for num in range(1, 100) if num % 2 == 0}

print(my_list1)
print(my_list2)
print(my_list3)

# Dictionary Comprehension
simple_dict = {"a": 1, "b": 2}

my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}

print(my_dict)


# Need a dictionary with key as number and value as square

my_dict1 = {item: item**2 for item in [1, 2, 3, 4, 5]}
print(my_dict1)
