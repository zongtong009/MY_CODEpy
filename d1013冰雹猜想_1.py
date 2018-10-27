from sympy import Symbol as Symbol
x = Symbol('x')
y = Symbol('y')

def bb(x):
    y = (3*x+1)/2
    if isinstance(y, float):
        y = int(y)
    return y

f=bb(x)

f7=bb(7)
print(f,'\n',f7,"  不能被2整除才行，例如7变11是奇数，肯定是增大的，但是如果是偶数一定比7小，就是减小了，没有了可能性",sep='')

f=bb(f)
print(f,"不能被4整除才行")
'''
for i in range(10):
    d=2**(i+1)
    print(f, "不能被%d整除才行" % d)
    f = bb(f)
''' '''
for i in range(7,8,2):
    f_i=bb(i)
    for ii in range(20):
        while f_i%2==0:
            f_i=int(f_i/2)
        d=2**(ii+1)     #2,4,8,16,32,...
        print(f_i, "不能被%d整除才行" % d)
        if f_i%d==0:
            print(i)
            break
        else:
            f_i = bb(f_i)
'''

