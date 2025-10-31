'''
打开Python文件夹中的test3.py文件，在其中编写程序解决如下问题
【问题描述】
输入n个学生的语文成绩,求其中成绩大于等于75的学生的人数及学生总数
【输入】
输入有n+1行,每行只有1个数,其中前n行中的数为学生的语文成绩;
第n+1行中的数为-1,表示输入结束
【输出】
输出只有1行,包含2个数,依次为成绩大于等于75的学生人数和学生总数,
数之间用1个空格分隔开
【输入/输出样例】
【输入】
80.5
90.0
70.5
60.5
95.0
76.5
-1
【输出】
4 6
'''
count_total = 0
count_above_75 = 0
while True:
    score = float(input())
    if score == -1:
        break
    count_total += 1
    if score >= 75:
        count_above_75 += 1
print(count_above_75, count_total)