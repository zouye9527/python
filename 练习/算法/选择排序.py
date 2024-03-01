def xzpx(b):
    c=b.split()
    a=[]
    for i in range(len(c)):
        a.append(int(c[i]))
    for i in range(len(a)):
        jmin=i
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
x=input("请输入一个整数序列，用空格隔开，以回车结束：")
xzpx(x)