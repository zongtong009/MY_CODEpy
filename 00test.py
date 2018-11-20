'''
本文件不具备保存意义，可以随意更改
'''

print(1)
# a = eval(input())
# 0 hgrfhr
# 0 hgrfh
# 0 hgrf
# 0 hgr
# 0 hg
# 0 h
# 1 grfhr
# 1 grfh
# 1 grf
# 1 gr
# 1 g
# 2 rfhr
# 2 rfh
# 2 rf
# 2 r
# 3 fhr
# 3 fh
# 3 f
# 4 hr
# 4 h
# 5 r


def fun(s):
    sum = 0
    len_a = len(s)
    for i in range(len_a+1):
        for j in range(i, len_a):
            for k in s[i:][: len_a - j]:
                if k in 'aeouiAEOUI':
                    sum += 1
    return sum


def sum_aeoui(str_string):
    # 计算单个字符串中元音字母数
    s = str_string.lower()
    sum = 0
    for t in s:
        if t in 'aeoui':
            sum += 1
    return sum


print(fun('baceb'))
