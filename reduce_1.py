''' reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
    但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
    reduce()对list的每个元素反复调用函数，并返回最终结果值。
'''
# reduce()还可以接收第3个可选参数，作为计算的初始值。
from functools import reduce


def prod(L):
    def mul(x, y):
        return x*y
    return reduce(mul, L)


def mul(x, y):
    return x * y


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print('3 * 5 * 7 * 9 =', reduce(mul, [3, 5, 7, 9]))
