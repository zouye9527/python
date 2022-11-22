"""
王老师要对两个小组的数学成绩进行对比，分别统计出两个小组中不及格(<60)学生的代号。
输入数据包括两行，第一行为第一小组每个人的成绩，第二行为第二小组每个人的成绩，输入时按照学生代号顺序输入，
第一个的代号为1，第二个的代号为2，依次类推。输出结果包括两行，第一行为第一小组中不及格学生的代号，第二行为第二小组不及格学生的代号。
输入样例
65 84 77 48 83 52 46 65 98 47 73 80
93 66 73 60 68 72 91 42 87 69 78 89
输出样例
4 6 7 10 
8
"""
data1=input().split()
data2=input().split()
data1_1=[]
data2_2=[]
for i in data1:
   data1_1.append(int(i))
for i in data2:
   data2_2.append(int(i))
for i in range(len(data1_1)):
   if data1_1[i]<60:
      print(i+1," ",end='')
print()
for i in range(len(data2_2)):
   if data2_2[i]<60:
      print(i+1,' ',end='')

