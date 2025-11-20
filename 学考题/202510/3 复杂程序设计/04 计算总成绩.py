'''
15. 打开Python文件夹中的test3.py文件，在其中编写程序解决如下问题
【问题描述】
计算机二班分为若干个学习小组，Python程序设计考试包括理论考试和上机考试两部分。编写程序，统计小组各成员的总成绩。
(注：总成绩=理论成绩×0.7+上机成绩×0.3)
【输入】
输入有n+1行，第1行只有1个整数n,表示小组人数，后面的n行，每行由3部分组成，依次是1名小组成员的名字、理论成绩和上
机成绩，3部分之间分别用1个空格隔开
【输出】
输出有n行，每行由两部分组成，依次是1名小组成员的姓名和总成绩（保留1位小数），两部分之间用1个空格隔开（输出顺序按输
入次序排列)
【输入/输出样例】
【输入】
5
张芳 80 85
刘晓红 88 90
王强 90 86
赵飞 76 71
李玲玲 85 87
【输出】
张芳 81.5
刘晓红 88.6
王强 88.8
赵飞 74.5
李玲玲 85.6
'''

n = int(input())
name=[]
total_score=[]
for i in range(n):
    data = input().split()
    name.append(data[0])
    theory_score = float(data[1])
    practical_score = float(data[2])
    total_score.append(theory_score * 0.7 + practical_score * 0.3)
for j in range(n):
    print(name[j], "%.1f" % total_score[j])