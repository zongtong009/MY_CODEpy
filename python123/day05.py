""" 埃拉托色尼筛选法


埃拉托色尼筛选法是一个很漂亮的示例算法。

在 i7 CPU（单线程）处理器下它可以在1s之内生成10 ^ 9以内的所有素数，因此，当这种筛选算法被应用的时候，它的速度是非常惊人的。

而我用了最基础的版本（未进行分割），仅仅只是删除了在数组中的偶数。
 """
import numpy as np


def eratosthenes(n):
    n = (n + 1) >> 1
    p = np.ones(n, dtype=np.int8)
    i, j = 1, 3

    while i < n:
        if p[i]:
            p[j * j >> 1::j] = 0
        i, j = i + 1, j + 2

    return p.sum()


res = eratosthenes(1000000)
print(res)
