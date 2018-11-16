a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
listA = []
listA.append(a[0])
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        listA.append(a[i])

print(listA)
