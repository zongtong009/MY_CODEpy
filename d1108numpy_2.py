import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print('我们的数组是：', a, '\n')

print('调用 mean() 函数：', np.mean(a))

print('沿轴 0 调用 mean() 函数：', np.mean(a, axis=0), '\n')

print('沿轴 1 调用 mean() 函数：', np.mean(a, axis=1), '\n')
