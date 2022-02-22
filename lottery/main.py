import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for i in range(5):
    #     print(random.sample(range(0, 9), 5))

    # print([1, 6, 9, 14, 19, 33, 9])
    # for i in range(4):
    #     print(sorted(random.sample(range(1, 34), 6))
    #           + random.sample(range(1, 17), 1)
    #           )

    print([1, 3, 7, 16, 19, 2, 12])
    for i in range(4):
        print(sorted(random.sample(range(1, 36), 5))
              + sorted(random.sample(range(1, 13), 2))
              )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
