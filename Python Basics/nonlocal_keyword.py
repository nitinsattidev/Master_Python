def outer():
    x = "local"

    def inner():
        nonlocal x  # This means that x is from parent
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
