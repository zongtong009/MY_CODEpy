# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print([list(random.sample(range(0, 9), 5)) for i in range(3)])
    print([list(random.sample(range(1, 34), 6)) + random.sample(range(1, 17), 1) for i in range(3)])
    print([list(random.sample(range(1, 36), 5)) + sorted(random.sample(range(1, 13), 2)) for i in range(3)])
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
Hi, [[0, 1, 3, 6, 7], [0, 5, 6, 7, 8], [0, 1, 5, 6, 7]]
[[25, 27, 10, 18, 26, 23, 3], [26, 2, 24, 9, 11, 22, 13], [2, 31, 5, 3, 33, 25, 16]]
[[19, 23, 10, 17, 22, 7, 9], [16, 35, 14, 30, 20, 6, 8], [17, 29, 12, 14, 13, 2, 5]] '''