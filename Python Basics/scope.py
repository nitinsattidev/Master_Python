# Scope - What variables do I have access to?

# whatever is defined in function, can't be used outside it

if True:
    x = 10


def some_func():
    total = 100


print(x)
# print(total) This can't be used because total is not defined globally


########################

a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())


# Rules
# 1 - Start with local#
# 2 - parent local?
# 3 - Global
# 4 - built in python functions


b = 1


def parent():
    b = 10

    def confusion():
        return b

    return confusion()


print(parent())
print(b)
