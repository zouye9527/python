"""
王老师要对成绩进行统计，根据输入的语文、数学和英语成绩，输出该名同学三科的总分。
输入样例：
5
001 78 89 89
002 79 87 78
003 100 92 95
004 98 98 89
005 89 86 87
输入的第一行中的数字5表明接下来要输入5名同学的学号和成绩，在接下来的5行中，“001、002、003……”分别是5名同学的学号，
每行中后面的三个数分别是三门课程的分数,每行中的数字之间以空格分隔
输出样例：
001 256
002 244
003 287
004 285
005 262
输出的学号和总分之间以空格分隔
"""
n=int(input())
cj=[]
for i in range(n):
    s=input()
    left1=s[:3]+" "
    right2=str(sum(map(int,s[3:].split())))
    cj.append(left1+right2)
for j in cj:
   print(j)
