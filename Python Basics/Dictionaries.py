# Dictionary
dictionary = {
    "a": 1,
    "b": 2,
}

print(dictionary["b"])


dictionary1 = {"a": [1, 2, 3], "b": 25, "phone": "123-456-7890"}

print(dictionary1["a"][2])


my_list = [
    {"a": [1, 2, 3], "b": 25, "phone": "123-456-7890"},
    {"a": [4, 5, 6], "b": 26, "phone": "098-765-4321"},
]

print(my_list[1]["a"][1])

# Dictionary keys always has to be immutable data types like strings, numbers, or tuples. Lists and dictionaries cannot be used as keys.
# Key in dictionary must be unique. If you try to use the same key again, it will overwrite the previous value.
