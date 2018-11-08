'''def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
r=list(r)


from functools import reduce

reduce(sum,[1, 3, 5, 7, 9])
#print(su)
'''

from functools import reduce


def fn(x, y):
    return x * 10 + y


re = reduce(fn, [1, 3, 5, 7, 9])
print(re)
