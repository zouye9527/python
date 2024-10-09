'''
王老师想要统计输入考生的数据中,有几名同学的成绩达到了
分数线(>=412)以上,输入时以—1表示结束。
输入：
001 568
002 390
003 474
004 389
005 378
006 498
007 536
008 617
009 367
010 550
-1
注:输入数据包含n+1行,其中前n行,每一行包含两部分,
中间以空格分隔,第一部分为学生的学号,第二部分为学生的整数成绩
输出：
001
003
006
007
008
010
6
注：逐行输出满足统计条件的同学的学号,
最后一行的数为满足条件的同学人数
'''
xh=[]   #学号
cj=[]   #成绩
num=0   #满足条件的人数
while True: #循环输入
    sc=input()  #输入学号和成绩
    if sc[0]=='-' and sc[1]=='1':   #判断是否为-1
        break   #跳出循环
    else:
        s1=sc.split()   #将字符串转换为列表
        xh.append(s1[0])    #将学号添加到列表中
        cj.append(int(s1[1]))   #将成绩添加到列表中


for i in range(len(cj)):    #遍历成绩列表
    if cj[i]>=412:  #判断成绩是否满足条件
        print(xh[i])    #输出满足条件的学号
        num+=1  #满足条件的人数加1
print(num)  #输出满足条件的人数

