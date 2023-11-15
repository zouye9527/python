'''
【问题描述】
育英中学组织男生进行了立定跳远的体育测试,现需要依据高中生体测标准（如下表所示）,评定男生立定跳远的等级情况和及格率,请编写程序完成此任务。

高中生体测标准表(男生)
项目		    优秀	良好	及格	不及格
50米跑(s)       <=7.0	7.1~8.0	8.1~9.0	>9.0
立定跳远(cm)    >=240	230~240	220~230	<220

【输入】
输入有n+1行,前n行每行有两部分,依次为姓名、立定跳远成绩（单位：厘米）,各部分之间用1个空格隔开。第n+1行只有1个—1,表示输入结束
【输出】
输出有n+1行,前n行每行有两部分,依次为姓名和等级,两部分之间用1个空格隔开,第n+1行只有一个数,表示及格率(保留2位小数)
【输入／输出样例】
【输入】 
李路 242
杨洋 230
周佳明 224
刘浩洋 235
吴涛 245
陈果 200
-1
【输出】
李路 优秀
杨洋 良好
周佳明 及格
刘浩洋 良好
吴涛 优秀
陈果 不及格
83.33%

'''

name=[]
score=[]
dengji=[]
while True:
    line=input()
    if line=='-1':
        break
    else:
        name.append(line.split()[0])
        score.append(int(line.split()[1]))
for i in range(len(score)):
    if score[i]>=240:
        dengji.append('优秀')
    elif score[i]>=230 and score[i]<240:
        dengji.append('良好')
    elif score[i]>=220 and score[i]<230:
        dengji.append('及格')
    else:
        dengji.append('不及格')
for i in range(len(name)):
    print(name[i],dengji[i])
x=0
for i in range(len(dengji)):
    if dengji[i]!='不及格':
        x+=1
for i in range(len(score)):
    print(name[i],dengji[i])
print('%.2f%%'%(x/len(score)*100))
