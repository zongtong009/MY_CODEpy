""" 二进制加法 有限状态机
按照在学校教授的那样可以完成二进制数的加法，只需要记住 1 + 1 = 10 并准寻一定的规则。

这个看似简单的算术却有很多话要说，例如，你可以看一下并行加法器的实现，其中有很多有趣的东西。

我决定通过有限状态机使用串行实现，基于输出 0/1 和进位 0/1 的组合有4种状态和基于输入位的转换组。

问题是真的需要四种状态吗？事实上只能使用三种状态，你能找到怎样的？
 """
import itertools

p0c0 = 0, {}
p1c0 = 1, {}
p0c1 = 0, {}
p1c1 = 1, {}

# transitions between states
p0c0[1].update({(0, 0): p0c0, (1, 0): p1c0,
                (0, 1): p1c0, (1, 1): p0c1})
p1c0[1].update({(0, 0): p0c0, (1, 0): p1c0,
                (0, 1): p1c0, (1, 1): p0c1})
p0c1[1].update({(0, 0): p1c0, (1, 0): p0c1,
                (0, 1): p0c1, (1, 1): p1c1})
p1c1[1].update({(0, 0): p1c0, (1, 0): p0c1,
                (0, 1): p0c1, (1, 1): p1c1})


def add(x, y):
    x = map(int, reversed(x))
    y = map(int, reversed(y))
    z = []
    # simulate automaton
    value, transition = p0c0
    for r, s in itertools.zip_longest(x, y, fillvalue=0):
        value, transition = transition[r, s]
        z.append(value)

    # handle carry
    z.append(transition[0, 0][0])

    return ''.join(map(str, reversed(z)))


print(add('1100100100100', '100100011000'))
