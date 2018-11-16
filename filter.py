def is_odd(n):
    return not n % 2 == 1


'''
filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，
    然后根据返回值是True还是False决定保留还是丢弃该元素，
    返回由符合条件元素组成的新list。
        filter()函数返回的是一个Iterator，也就是一个惰性序列，
        所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''
listA = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(listA)


def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
