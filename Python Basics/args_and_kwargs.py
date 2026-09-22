# *args   **kwargs


def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args), sum(kwargs.values())


print(super_func(1, 2, 3, 4, 5, 7, 8, 9, num1=5, num2=15))

# Rule: params, *args, default parameters, **kwargs
