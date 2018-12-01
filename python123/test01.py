"""
    次文件可进行随意更改，主要用于运行测试
"""

from decimal import Decimal, getcontext

getcontext().prec = 17

result = 3 * Decimal(0.1)
print(Decimal(0.1))
print(Decimal(0.2))
print(Decimal(0.1+0.2))

print(3 * 0.1)

