# Iterable - list, dictonary, tuple, set, string

# Iterate -> one by one check each item in collection

user = {"name": "Gollem", "age": 5003, "can_swim": False}

for item in user:
    print(item)

for item1 in user.items():
    print(item1)

for item2 in user.values():
    print(item2)

for item3 in user.keys():
    print(item3)

for item4 in user.items():  # or for key, value in user.items():
    key, value = item4
    print(key, value)
