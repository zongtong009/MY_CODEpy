strs = "((())))())))()((("
ls = []  # 过程量
id_left = []  # 左括号id
id_right = []  # 右括号id
for i, item in enumerate(strs):
    if item == "(":
        ls.append(item)
        id_left.append(i)
        # print(ls,end='')
    elif ls != []:
        ls.pop()
        id_left.pop()
        # print('\t',ls,end='')
    else:
        id_right.append(i)  # id从0开始
    #     print('\t\t',ls,end='')
    # print()
print('\n',id_left, id_right)
