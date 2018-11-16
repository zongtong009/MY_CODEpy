import random
stack = [1, 2, 3, 4, 5]
num = 0
while True:
    random.shuffle(stack)
    ja, yi, bi, di, wu = stack

    if 3 == (ja != 5) + (bi == 3) + (ja > wu) + (wu == 2) + (di != 1):
        cheat_man = 0
        if (ja != 5) is False and ja <= 2:
            cheat_man += 1
        if (bi == 3) is False and yi <= 2:
            cheat_man += 1
        if (ja > wu) is False and bi <= 2:
            cheat_man += 1
        if (wu == 2) is False and di <= 2:
            cheat_man += 1
        if (di != 1) is False and wu <= 2:
            cheat_man += 1
        if cheat_man == 2:
            print(ja, yi, bi, di, wu)
            break

#   ja  yi  bi  di  wu
#   4   1   5   2   3
#   T   F   T   F   T
