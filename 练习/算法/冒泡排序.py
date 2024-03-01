def mppx(b):
    c=b.split()
    a=[]
    for i in range(len(c)):
        a.append(int(c[i]))
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print("已经是有序的了")
    for i in range(len(a)):
        print(a[i],end=' ')
    return
x=input("请输入一个整数序列，用空格隔开，以回车结束：")
mppx(x)