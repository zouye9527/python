'''
【问题描述】
某公司招聘考试的总成绩由笔试成绩和面试成绩两部分组成,笔试成绩占60%,面试成绩占40%,编程输出所有应聘者总成绩的平均值a,及总成绩高于a的应聘者姓名
【输入】
输入有n+1行,前n行中每行包含三部分,依次为应聘者的姓名、笔试成绩、面试成绩,三部分之间用1个空格隔开；第n+1行只有一个-1,表示输入结束
【输出】
输出有m+1行,第一行只有一个数,表示所有应聘者的平均成绩a（保留2位小数）,后面的m行,每行只有一个应聘者的姓名,为成绩高于平均成绩a的应聘者姓名（若有多个,应聘者姓名的输出顺序按输入次序排列）
【输入/输出样例】 
【输入】 
张三 80 60
李四 90 70
赵六 70 80
王五 80 70
郑一 90 80
-1
【输出】 
78.00 
李四 
郑一

'''
name=[]
s=[]
while True:
    a=input()
    if a=='-1':
        break
    else:
        b=a.split()
        name.append(b[0])
        temp=[]
        for i in range(1,3):
            temp.append(float(b[i]))
        s.append(temp[0]*0.6+temp[1]*0.4)
avg=sum(s)/len(s)
print('%.2f'%avg)
for i in range(len(s)):
    if s[i]>avg:
        print(name[i])