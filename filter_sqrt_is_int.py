import math


def is_sqr(x):
    a = math.sqrt(x)
    return a == int(a)
    # return a*a == x


print(filter(is_sqr, range(1, 101)))
