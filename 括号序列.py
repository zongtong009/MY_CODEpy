strs = "((()))())))()((("  # "()))(("  # "((()))()(()((("
# list_strs = list(strs)  # 给定值不得改变
#  list_plus = []
# num_r = 0
# while True:
#     '''去掉最右侧 左括号  '''
#     if list_strs[len(list_strs)-1] == "(":
#         # list_plus.append(list_strs.pop())
#         list_strs.pop()
#         num_r += 1
#     else:
#         # print(list_strs)
#         break
#     print(list_plus)
# # 此时 list_strs = ( ) ) )
ls = []  # 过程量
id_left = []  # 左括号id
id_right = []  # 右括号id
for i, item in enumerate(strs):
    if item == "(":
        ls.append(item)
        id_left.append(i)
    elif ls != []:
        ls.pop()
        id_left.pop()
    else:
        id_right.append(i)  # id从0开始
        print(ls)
print(id_left, id_right)
"""

先去掉最右边 "(" ,这样只剩下 (   )   )   )
同时消掉相邻( ) ， 只剩下 )  ) 或只剩下 (  (  (
取得他们的id,再进行计算
"""
#   (   )   )   )   (   (
# (   (               )   )
# 0   1   2   3   4   5   6
# 1   2   5   5   3   4   1
