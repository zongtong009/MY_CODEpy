import random
strs = ''
for i in range(4):
    num = random.randint(0, 3)
    if num == i:
        str_num = str(random.randint(0, 9))
    else:
        str_num = chr(random.randint(65, 90))
    strs += str_num

print(strs)
