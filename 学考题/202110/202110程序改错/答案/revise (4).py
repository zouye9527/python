"""
小明编写了一个程序revise.py，从键盘上输入华氏温度，输出相对应的摄氏温度。
代码中存在错误，请帮助修改。
注：华氏温度（F）和摄氏温度（C）的转换公式C=(F-32)÷1.8，结果保留一位小数
输入样例：
100
输出样例：
相对应的摄氏温度为：37.8
"""
F=eval(input())
C=(F-32)/1.8
print("相对应的摄氏温度为：%.1f"%C)
