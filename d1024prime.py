from math import sqrt

def is_prime(x):
    if x==1:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

for i in range(1,100):
    #print(i," is",is_prime(i))
    print(i,'是质数')  if is_prime(i) else print(i,'不是质数')

