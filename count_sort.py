
list_alpha = [12, 5, 36, 52, 12, 5, 42, 34, 11, 7, 26, 34, 51, ]
dicA = dict()
print(dicA)
# dic_a = dict([(x, 0) for x in list_a])
# print(dic_a)

for i in list_alpha:
    dicA[i] = dicA.get(i, 0)+1
print(dicA)
