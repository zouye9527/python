"""
小张编写了一个程序revise.py，根据键盘上输入的分数，输出成绩情况，
大于80分，输出优秀；小于等于80分并且大于等于60分，输出及格；小于60分，输出分数，
并输出不及格。比如输入57，则输出“57 不及格”，分数和“不及格”之间有一个空格。
"""
score=eval(input())
if score>80:
    print("优秀")
elif score>=60:
    print("及格")
else:
    print(score,"不及格")
