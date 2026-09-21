# Tuple

# tuples are immutable sequences, typically used to store collections of heterogeneous data. They are defined by enclosing the elements in parentheses ().

my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple[1])

print(5 in my_tuple)  # This will return True because 5 is an element in the tuple.

user = {(1, 2): [1, 2, 3], "greet": "hello", "age": 32}

print(user[(1, 2)])

new_tuple = my_tuple[1:2]
print(new_tuple)

x, y, z, *other = my_tuple

print(x)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
