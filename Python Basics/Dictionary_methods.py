# Dictionary

user = {"basket": [1, 2, 3], "greet": "Hello", "age": 20}

print(user.get("temperature"))

print(user.get("greet"))

print(
    user.get("age", 55)
)  # If the key is not found, it will return the default value provided (55 in this case).


# Another way to create a dictionary is by using the dict() constructor.

user2 = dict(name="Nitin", age=32, weight=93)

print(user2)


# Another wayt to check if a key exists in a dictionary is by using the 'in' keyword.

print("greet" in user)

print(
    "hello" in user.keys()
)  # This will return False because "hello" is not a key in the dictionary.


print(user.items())

# user.clear()  # This will remove all items from the dictionary.

user3 = user.copy()  # This will create a shallow copy of the dictionary.

print(user)
print(user3)

print(
    user3.pop("age")
)  # This will remove the key "age" from the dictionary and return its value.

print(user3)


print(user3.popitem())
print(
    user3
)  # This will remove and return the last inserted key-value pair from the dictionary.


print(
    user3.update({"age": 28})
)  # This will update the value of the key "age" to 28 in the dictionary.
print(user3)
