""" 后缀表达式
虽然人们主要使用代数表达式中的中缀表达式记法，但是逆波兰表达式（也叫后缀表达式）更容易在算法上进行解析。

中缀表达式：二元运算符总是置于与之相关的两个运算对象之间，比如 1 + 2 ，2 * 4

后缀表达式：二元运算符置于其运算对象之后，比如 1 2 + ，2 4 *

例如，下面的表达式是等价的，第一个是中缀表达式，第二个是后缀表达式。

2 * (1 + 3) = 2 1 3 + *

当你实现你的第一个表达式解析器时，后缀和前缀表示法是最好的方法。对应到栈就是：入栈，出栈...

栈的学习：参考 Python 数据结构 —— 栈
"""
ops = {
    '+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '^': float.__pow__,
}


def postfix(expression):
    stack = []

    for x in expression.split():
        if x in ops:
            x = ops[x](stack.pop(-2), stack.pop(-1))
        else:
            x = float(x)
        stack.append(x)

    return stack.pop()


postfix('1 2 + 4 3 - + 10 5 / *')  # 相当于计算 ((1+2)+(4-3))*(10/5)
