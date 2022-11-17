"""
小王编写了一个程序revise.py，根据键盘上输入的分数，输出成绩等级，
成绩>=90分是A等级，60-89分（含）之间是B等级，60分以下是C等级。
代码有错误，请帮助修改。
"""
score = eval(input())
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print(grade)
