# Two concepts of functional programming
# 1. Will provide same out put for same input everytime
# 2. Doesn't interact witn extermal world
# 3. Keep functions and data separate

# Pure Functions


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)

    return new_list


print(multiply_by2([1, 2, 3]))
