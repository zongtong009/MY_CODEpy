# n = int(input('请输入一个整数:'))
# dic = {0: 0, 1: 1}
# a = 0
print("             递归次数", sep="")


def fib(num):
    """
    字典法

    """
    if num in dic:
        return dic[num]
    else:
        temp = fib(num - 1) + fib(num - 2)
        dic[num] = temp
        return temp


def fab(num):  # 纯递归计算
    global a
    if num < 1:
        print('输入有误！')
        return -1
    if num == 1:
        a += 1
        print("f(1)          = 1", a, sep=" ")
        return 1
    elif num == 2:
        a += 1
        print("f(2)          = 2", a, sep=" ")
        return 1
    # elif num == 3:
    #     return 2
    # elif num == 4:
    #     return 3
    else:
        fin = fab(num - 2) + fab(num - 1)
        a += 1
        print("f(%d)=f(%d)+f(%d)=" % (num, num - 2, num - 1), fin, a)
        return fin


for i in range(10):
    n = int(input('请输入一个整数:'))
    if not n:
        break
    a = 0
    print(fab(n))
# for i in range(n):
#     print(dic, fib(i + 1), end="\n")
