from math import sqrt


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x))+1):
        # 2/1+1 3/1+1 4/2+1 5/2+1 ... 9/3+1 10/3+3
        if x % i == 0:
            return False
    return True


for i in range(1, 100):
    # print(i," is",is_prime(i))
    print(i, '是质数') if is_prime(i) else print(i, '不是质数')
