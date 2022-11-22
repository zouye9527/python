"""
小王在实验室中设计了两种实验方案，得到了如下的两组实验数据：
58 29 50 4 75 16 96 12 2 72
85 37 43 56 69 80 43 8 97 33
其中，第一行为方案一数据，第二行为方案二数据，其中数值>=60的即为有效数据，每组数据个数大于等于5，小于等于20。
我们已知方案的有效率=有效数据个数/数据总个数×100%。
请编写程序，比较两种方案，如果方案二的有效率>=方案一的有效率，则输出“good”，否则输出“bad”。
输入样例：
58 29 50 4 75 16 96 12 2 72
85 37 43 56 69 80 43 8 97 33
输出样例：
good
"""
data1=input().split()
data2=input().split()
data01=[]
data02=[]
n1=0
n2=0
for i in range(len(data1)):
    data01.append(int(data1[i]))
for i in range(len(data2)):
    data02.append(int(data2[i]))
for i in data01:
    if i>=60:
        n1+=1
for i in data02:
    if i>=60:
        n2+=1
yxl1=n1/len(data01)
yxl2=n2/len(data02)
if yxl2>=yxl1:
    print("good")
else:
    print("bad")
