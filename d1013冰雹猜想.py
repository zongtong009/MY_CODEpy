max = 1
ls = []
lss = []
for num in range(2, 8):
    num_1 = num
    print('\n', num, sep='')
    while True:
        if num == 1:
            break
        if num % 2 == 0:
            num = int(num/2)
        else:
            num = num*3+1
        print(num, end=' ')
        if num > max:
            max = num
            if num_1 not in ls:
                ls.append(num_1)
                lss.append(max)
            else:
                lss.pop()
                lss.append(max)
print('\n', ls, '\n', lss, sep='')

# (3x+1)/2) *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2 *3+1)/2
