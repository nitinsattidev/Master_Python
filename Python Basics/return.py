def sum(num1, num2):
    return num1 + num2


print(sum(4, 6))

# function should do one thing really well
# should return something
# return keyword automatically exits th function
#################


def sum1(num1, num2):
    def another_func(anothernum1, anothernum2):
        return anothernum1 + anothernum2

    return another_func(num1, num2)


total = sum1(10, 30)
print(total)
