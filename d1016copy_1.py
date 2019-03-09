import copy
deepcopy = copy.deepcopy
a = [1, 2, 3, 4, [5, 6]]
b = deepcopy(a)

print(id(a), id(b))

a[4][1] = 66

print(id(a), id(b))
print(a, b, sep='\n')
