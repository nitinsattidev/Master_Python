li = [1, 2, 3, 4, 5]
li2 = ["a", "b", "c", "d", "e"]
li3 = [1, 2, "a", True]

# Data Structure

# List slicing

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]

print(amazon_cart[0:2])
print(amazon_cart[0::2])

# Lists are Mutable
amazon_cart[0] = "laptop"
new_cart = amazon_cart[0:3]
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

new_cart = amazon_cart  # This isn't copy
new_cart[0] = "ship"
print(new_cart)
print(amazon_cart)


new_cart = amazon_cart[:]  # This is copy
new_cart[0] = "table"
print(new_cart)
print(amazon_cart)
