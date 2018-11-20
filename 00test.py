'''
本文件不具备保存意义，可以随意更改
'''

print(1)
a = eval(input())
test_dict = {
    1: 'WS', 6: 'WS', 7: 'WS', 12: 'WS',
    2: 'MS', 5: 'MS', 8: 'MS', 11: 'MS',
    3: 'AS', 4: 'AS', 9: 'AS', 10: 'AS',
}
for i in range(a):
    m = eval(input())
    m_value = test_dict[m]
    quotient = m//12  # 商
    remainder = m % 12  # 余数
    m_correspond = quotient+12-remainder
    print(m_correspond, m_value)
