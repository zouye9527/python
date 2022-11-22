"""
王老师要对两个小组的数学成绩进行对比，分别计算出两个小组及格率（及格为成绩≥60）的差异。
输入的第一行为第一小组每个人的成绩，
第二行为第二小组每个人的成绩，
在一行中输出两个小组的及格率分别为多少，输出结果保留一位小数。
输入样例
50 4 75 16 96 12 2 72 56 32
43 56 69 80 43 8 97 33 56 68
输出样例
30.0% 40.0%
"""
data1=input().split()
data2=input().split()
data1_1=[]
data2_2=[]
n=0
m=0
for i in data1:
    data1_1.append(int(i))
for i in data2:
    data2_2.append(int(i))

for i in range(len(data1_1)):
    if data1_1[i]>=60:
        n+=1
for i in range(len(data2_2)):
    if data2_2[i]>=60:
        m+=1
jgl1=n/len(data1_1)*100
jgl2=m/len(data2_2)*100
print("%.1f%%"%jgl1,"%.1f%%"%jgl2)