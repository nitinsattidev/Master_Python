basket = [1, 2, 3, 4, 5]
test = [20, 30, 40, 50]
bucket = ["a", "w", "b", "x", "c", "d", "e"]
# print(len(basket))  # Output: 5

# Adding

new_list = basket.append(100)
print(new_list)
print(basket)

basket.insert(4, 200)
new_list = basket

print(new_list)
print(basket)

basket.extend([101, 201, 310])
print(basket)
print(new_list)


####################### remove
print(basket)
basket.pop()
print(basket)
basket.pop(0)
print(basket)

basket.remove(100)
print(basket)


print(test)
test.clear()
print(test)


########### index

print(bucket.index("c"))

print(
    bucket.index("d", 0, 6)
)  # This will raise a ValueError since 'd' is not in basket

print("c" in bucket)
print("x" in bucket)

print(bucket.count("c"))

bucket.sort()
print(bucket)


bucket = ["a", "w", "b", "x", "c", "d", "e"]

new_bucket = bucket[:]  # or new_bucket = bucket.copy()
bucket.sort()
print(bucket)
print(new_bucket)

bucket.reverse()
print(bucket)


print(list(range(100)))
