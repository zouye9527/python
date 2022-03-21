"""
小明编写了一个程序revise.py，从键盘上输入n的值，计算出1+2+3+……+n的值。
代码中存在错误，请帮助修改。
"""
n=eval(input())
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print(s)

