n=int(input("请输入n："))
a=0
b=1
m=0
while m<n:
    a=a+b
    b=b+a
    m=m+1
print(a,b,m)