# formatted strings

name = "Nitin"
age = 32

print(f"Hi {name}, your age is {age}")

# or

print("Hi {}, your age is {}".format(name, age))

# or

print("Hi {1}, your age is {0}".format(name, age))

# or

print("Hi {name}, your age is {age}".format(name="Chandra", age=65))
