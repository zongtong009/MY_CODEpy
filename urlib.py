from urllib import request

response = request.urlopen("http://www.baidu.com/")  # 打开网站

with open("urllibtxt.txt", 'w') as fi:      # open一个txt文件
    page = fi.write(str(response.read()))   # 网站代码写入
    print(page)