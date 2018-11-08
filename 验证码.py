import random
str_s = ''
for i in range(4):
    num = random.randint(0, 3)
    if abs(num-i) > 1:
        str_num = str(random.randint(0, 9))
    else:
        str_num = chr(random.randint(65, 90))
    str_s += str_num

print(str_s)
