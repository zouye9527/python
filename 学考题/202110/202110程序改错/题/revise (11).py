"""
小张编写了一个程序revise.py，根据键盘上输入的n的值，
输出1到n（含）之间3的倍数的正整数的和。
代码中存在错误，请帮助修改。
"""
n=eval(input())
s=0
for i in range(1,n+1)：
    if i%3==0:
        s=s+i
print(s)
        
