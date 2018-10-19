a=[1,2,3,[4,5]]
b=a
print(id(a))
print(id(b))
b[3][1]=6
print(id(a))
print(id(b))
a=list(a)
print(id(a))
print(id(b))


