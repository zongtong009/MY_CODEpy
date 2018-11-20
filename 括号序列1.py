#   (   )   )   )   (   (    原始数据
# 得到下列未匹配括号位置
#           )   )   (   (
# (   (               )   )
# 插入括号的id
# 0   1   2   3   4   5   6

strs = "()))(("
cost = [1, 2, 5, 5, 3, 4, 1]
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
    else:
        id_right.append(i)  # id从0开始
        # print('\t\t',ls,end='')
print('\n', '单左括号id', id_left, '单右括号id', id_right)

right_cost = list(cost[0:id_right[-1]+1])  # 由最后一个右括号判断
left_cost = list(cost[id_left[0] + 1:])  # 由第一个左括号来判断


def get_min(my_list):
    min = my_list[0]
    for item in my_list:
        if item < min:
            min = item
    my_list.remove(min)
    return min


'''    对右括号对应list取两个最小值 '''
rmin_a = get_min(right_cost)
rmin_b = get_min(right_cost)
'''    对左括号对应list取两个最小值 '''
lmin_a = get_min(left_cost)
lmin_b = get_min(left_cost)
sum = rmin_a + rmin_b + lmin_a + lmin_b
print('最小代价为: ', sum)
