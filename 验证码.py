import random
import time
random.seed(time.time()%1)  # 随机种子
str_s = ''
for i in range(4):
    num = random.randint(0, 4)  # 0,1,2,3
    if num <= 1:  
        str_num = str(random.randint(0, 9))
    elif num == 3:
        str_num = chr(random.randint(65, 90))
        # 大写字母 A-Z
    else:   
        str_num = chr(random.randint(97, 112))
        # 小写字母 a-z
    str_s += str_num

print(str_s)
