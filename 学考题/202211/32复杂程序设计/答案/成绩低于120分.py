'''
统计哪些同学的语文成绩低于120分（＜120），并统计有几名同学的成绩低于120分输入：
5 
001 123 
002 102 
003 121 
004 132 
005 98
注：输入数据包含n+1行(n<=50),第一行的数为n，表示下面要输入n名同学的数据，接下来的n行数据，以空格分隔，
第一个数据为学生的考号，第二个数据为学生的语文成绩，成绩为整数
输出： 
002 
005 
2
注：分行输出满足条件的同学的考号，最后一行为有几名同学成绩低于120分
'''
n=int(input())
s1=[]
s2=[]
m=0
for i in range(n):
    s=input().split()
    s1.append(s[0])
    s2.append(int(s[1]))
for i in range(n):
    if s2[i]<120:
        print(s1[i])
        m+=1
print(m)

