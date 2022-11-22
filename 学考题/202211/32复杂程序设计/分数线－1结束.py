'''
王老师想要统计输入考生的数据中，有几名同学的成绩达到了2021年河北省本科批次物理科目组合的分数线（>=412）以上。输入时以—1表示结束。输入：
ZHAO 568 
QIAN 390 
SUN 474 
LI389 
ZHOU 378 
WU 498 
ZHENG 536 
WANG 617 
FENG 367 
CHEN 550 
-1
注：输入数据共n＋1行（n<=50)，前面的n行数据，每一行包含两部分，中间以空格分隔，第一个数据为学生的名字，第二个数据为学生的整数成绩
输出：
ZHAO
SUN 
WU 
ZHENG 
WANG 
CHEN 
6
注：逐行输出满足统计条件的同学的名字，最后一行的数为满足条件的同学人数
'''
m=0
s2=[]
while True:
    s=input()
    if s[0]=="-" and s[1]=="1":
        break
    else:
        s1=[]
        s1=s.split()
        if int(s1[1])>=412:
            m+=1
            s2.append(s1[0])
for i in s2:
    print(i)
print(m)

