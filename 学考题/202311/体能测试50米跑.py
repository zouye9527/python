'''
【问题描述】
育英中学组织男生进行了50米跑项目的体育测试,现需要依据高中生体测标准(如下表所示),评定男生50米跑的等级情况和及格率,请编写程序完成此任务。

高中生体测标准表(男生)
项目		    优秀	良好	及格	不及格
50米跑(s)       <=7.0	7.1~8.0	8.1~9.0	>9.0
立定跳远(cm)    >=240	230~240	220~230	<220

【输入】
输入有n+1行,第1行只有1个整数n,表示需要计算的学生数,接下来的n行,每行有两部分,依次为姓名、50米跑成绩(单位：秒),各部分之间用1个空格隔开
【输出】
输出有n+1行,前n行每行有两部分,依次为姓名和等级,两部分之间用1个空格隔开,第n+1行只有一个数,表示及格率(保留2位小数)

【输入／输出样例】
【输入】 
6
李路 7.8
杨洋 6.2
周佳明 6.5
刘浩洋 8.1
吴涛 9.2
陈果 7.5
【输出】
李路 良好
杨洋 优秀
周佳明 优秀
刘浩洋 及格
吴涛 不及格
陈果 良好
83.33%
'''
name=[]
score=[]
classes=['优秀','良好','及格','不及格']
n=int(input())
for i in range(n):
    line=input()
    name.append(line.split()[0])
    score.append(float(line.split()[1]))
for i in score:
    if i<=7.0:
        print(name[score.index(i)],'优秀')
    elif i<=8.0:
        print(name[score.index(i)],'良好')
    elif i<=9.0:
        print(name[score.index(i)],'及格')
    else:
        print(name[score.index(i)],'不及格')
x=0
for i in score:
    if i<=9.0:
        x+=1
jgl=x/n*100
print('%.2f%%'%jgl)

    