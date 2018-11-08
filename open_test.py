'''f = open("forwrite.txt", "w+",encoding='utf-8')
f.write("可以，你做的很好！6666")  # 此时文件对象在最后一行，如果读取，将读不到数据
s=f.tell()     # 返回文件对象当前位置
f.seek(0,0)    # 移动文件对象至第一个字符
str=f.read()
print(s,str,len(str))

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('test')
'''
fl = open("H:\\tr.txt", "r", encoding='utf-8')
for line in fl.readlines():  # 依次读取每行
    line = line.strip()  # 去掉每行头尾空白
    print("读取的数据为: %s" % (line))
print()
fl.close()
# 读
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        print("读取的数据为: %s" % (line))

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():  # 依次读取每行
        # line = line.strip()                             #去掉每行头尾空白
        print("读取的数据为: %s" % (line))

print("//n\\n")
