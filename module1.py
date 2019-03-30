import time

def main():
    print("mo dule")
    print('按下回车开始计时，按下 Ctrl + C 停止计时。')
    starttime = 0
    while True:
        input() # 如果是 python 2.x 版本请使用 raw_input()
        try:
            #input() # input()写在这会报错
            starttime = time.time()
            print('开始')
            while True:
                time.sleep(0.1)
                print('计时: ', round(time.time() - starttime, 2), '秒', end="\r")
        except KeyboardInterrupt:
            endtime = time.time()
            print('结束')
            if starttime == 0:
                break
            print('总共的时间为:', round(endtime - starttime, 2),'secs')
            break
if __name__ == "__main__":
    main()