"""下一组排列
此时我们被给定一个全序集，要找到当前结构的下一组排列，如：FADE -> FAED -> FDAE -> FDEA -> ...

尽管几乎每一个库里都提供了类似的功能，但若是你想要提高算法速率的话，还是得看看这个。

这个算法本身是非常简单的：

从序列的末尾开始，找到递减的最长子序列（如：42531）且将它前面的项表示为一个支点（如：42531）。
将此支点与找到的递减最长子序列中的次小项进行交换（如：43521）。
将递减子序列转向（如：43125）。
"""


def permute(values):
    n = len(values)

    # i: position of pivot
    for i in reversed(range(n - 1)):
        if values[i] < values[i + 1]:
            break
    else:
        # very last permutation
        values[:] = reversed(values[:])
        return values

    # j: position of the next candidate
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            # swap pivot and reverse the tail
            values[i], values[j] = values[j], values[i]
            values[i + 1:] = reversed(values[i + 1:])
            break

    return values


permute(list('FADE'))
