# MRO - Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.mro())

print(D.num)

print("#########################")


class X:
    pass


class Y:
    pass


class Z:
    pass


class E(X, Y):
    pass


class F(Y, Z):
    pass


class G(F, E, Z):
    pass


print(G.__mro__)
