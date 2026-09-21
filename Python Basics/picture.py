# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for image in picture:
    pixel = 0
    while pixel < len(image):
        if image[pixel] == 1:
            print("*", end="")
        else:
            print(" ", end="")
        pixel += 1
    print("")


# clean
# Readability
# predictability
