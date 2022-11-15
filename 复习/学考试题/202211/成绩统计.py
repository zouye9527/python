# 打开素材文件夹中的python＼test3．py，在该文件中完成程序。
# 小王想要统计本班某次语文考试，有几位同学的成绩与班级平均分的差距超过5分（＞5）。
# 输入
# 10 
# 90 
# 92 
# 98 
# 89 
# 80 
# 132 
# 110 
# 91 
# 88 
# 102
# 注：输入数据共n＋1行（n<=50），第一行的数为同学人数n，接下来的n行，每行一个整数，为每位同学的成绩
# 输出
# 8
# 注：输出一个整数 
n=int(input())
sc=[]
for i in range(n):
    sc.append(int(input()))
avg=sum(sc)/n
m=0
for i in range(n):
    if abs(sc[i]-avg)>5:
        m=m+1
print(m)




