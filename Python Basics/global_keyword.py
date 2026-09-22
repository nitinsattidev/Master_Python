total = 0


def count():
    global total
    total += 1
    return total


print(count())


def count1(total):

    total += 1
    return total


print(count1(count1(count1(total))))
