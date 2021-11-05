# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for k in range(1000):
        for n in range(1000):
            if k * (k + 1) * (2 * k + 1) < n < (k + 2) * (k + 1) * (2 * k + 3):
                print(n, k)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
