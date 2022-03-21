"""
小王编写了一个程序revise.py，根据键盘上输入的a和b的值，判断a是否能被b整除。
代码有错误，请帮助修改。
测试
输入样例1：
100
3
输出样例1：
False
输入样例2：
100
2
输出样例2：
True
"""
def  ceshi(a,b):
    if a%b==0:
        return True
    else:
        return False
a=eval(input())
b=eval(input())
print(ceshi())
    
