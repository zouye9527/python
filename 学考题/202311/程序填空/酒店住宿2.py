'''
某高校的n名男生打算暑期一起出去旅游,出发前需要安排好酒店住宿,
已知当地4人间为160元/间,3人间为140元/间,在保证每人都有床位的情况下,怎样订房间最省钱。
小王编写了如下的程序,其中①处应填写()
'''
#完整代码
n=int(input('请输入人数：'))
Mmin=160*n
for r4 in range(n//4+1):  #①
    rs=n-4*r4
    if rs%3==0:      #②
        r3=rs//3
    else:
        r3=rs//3+1   #③  
    w=160*r4+140*r3
    if Mmin>w:       #④
        Mmin=w
        f3=r3
        f4=r4
print("四人间：",f4,"三人间：",f3,"最少费用：",Mmin)