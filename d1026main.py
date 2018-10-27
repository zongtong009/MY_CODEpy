#注释
a=1
def main():
    print("Hello,World!")
    global a
    a+=1
    print(a)

def ss():
    print("Hello,World!",)
s=ss
f=s.__name__


if __name__=='__main__':
    main()
    print(f)