""" 矩阵链乘法
矩阵乘法是一个满足结合律的运算。显然，对于矩阵A、B、C来说，(AB)C 与 A(BC) 是等价的，我们可以根据自己的心情选择任意的运算顺序，总之，结果都是一样的。

糟糕的是，对计算机来说可不是这么回事，若我们假定矩阵 A = [10, 20], B = [20, 30], C = [30, 40]，那么在以下两种运算顺序中，标量相乘的次数是天差地别：

(AB)C = 10*20*30 + 10*30*40 = 18000

A(BC) = 20*30*40 + 10*20*40 = 32000

我们可以使用递归关系来找到我们需要的最优解法，首先，我们要用一个函数MCM来得到最小标量相乘次数，那么MCM也可用来定义在所有情况下的最优子段，则：


再使用动态规划和备忘录法即可得到结果，时间复杂度为O(n³)。
 """


def mult(chain):
    n = len(chain)

    # single matrix chain has zero cost
    aux = {(i, i): (0,) + chain[i] for i in range(n)}
    # i: length of subchain
    for i in range(1, n):
        # j: starting index of subchain
        for j in range(0, n - i):
            best = float('inf')
            # k: splitting point of subchain
            for k in range(j, j + i):
                # multiply subchains at splitting point
                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[k + 1, j + i]
                cost = lcost + rcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                # pick the best one
                if cost < best:
                    best = cost
                    aux[j, j + i] = cost, var, lrow, rcol
    return dict(zip(['cost', 'order', 'rows', 'cols'], aux[0, n - 1]))


print(mult([('A', 10, 20), ('B', 20, 30), ('C', 30, 40)]))


""" 备注：

动态规划是一种将问题实例分解为更小的、相似的子问题，并存储子问题的解而避免计算重复的子问题，以解决最优化问题的算法策略。

备忘录法是动态规划方法的变形。与动态规划算法不同的是，备忘录方法的递归方式是自顶向下的，而动态规划算法则是自底向上的。
 """