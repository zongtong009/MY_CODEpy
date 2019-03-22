import copy


def fun(lst):
    # result = 0
    # lst_plus = copy.deepcopy(lst)
    # for item in lst:
    #     lst_plus.remove(item)
    #     if item in lst_plus:
    #         result += 1
    # return result
    if len(set(lst)) == len(lst):
        return 0
    return len(lst) - len(set(lst))


s_temp = [4, 5, 12, 6, 78, 24, 5, 78]

print(fun(s_temp))
