def fun(i):
    while i:
        if i%2==0:
            print("i=",i)
            yield 2
            i-=1
            print("-------------------","\n")
            
        if i%2==1:
            print("i=",i)
            yield 1
            i-=1
            print("-------------------","\n")
        
for i in fun(10):
    print("return=",i,sep="")
