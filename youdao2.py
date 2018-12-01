# if __name__ == "__main__":
#     main()
import tkinter as tk
import requests

window = tk.Tk()
window.title("主人的翻译器")
window.geometry("550x200+300+270")  # 长乘高

'''label标签栏'''
l0 = tk.Label(window, text="输入内容", font="微软雅黑 15", height=2)
l0.grid()
l1 = tk.Label(window, text="翻译", font="微软雅黑 15", height=2)
l1.grid()
# l2 = tk.Label(window, height=2)
# l2.grid()

var = tk.StringVar()
'''text文本框'''
e = tk.Entry(window, width=50)
e.grid(row=0, column=1)
e1 = tk.Entry(window, textvariable=var, width=50)
e1.grid(row=1, column=1)


def click():
    content = e.get()
    if content == '':
        return
    data = {
        "i": content,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    response = requests.post(
        "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule", data=data).json()
    bb = response["translateResult"][0][0]["tgt"]
    # print(bb)
    # print(type(bb))
    var.set(bb)


b0 = tk.Button(window, text="点击翻译", command=click, width=15, font="微软雅黑 12")
b0.grid()
b1 = tk.Button(window, text="退出", command=window.quit, width=15, font="微软雅黑 12")
b1.grid(row=2, column=1)
# b2 = tk.Button(window, width=15, font="微软雅黑 12")
# b2.grid(row=2, column=1)

window.mainloop()
