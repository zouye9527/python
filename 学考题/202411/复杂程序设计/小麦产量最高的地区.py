'''
【问题描述】
某省有n个地区,输入各地区的名称及其小麦产量,编写程序输出该省小麦产量最高的地区名称（可能有多个）
【输入】
输入有n+1行,第一行只有1个整数,表示地区总数n;接下来的n行每行包含两部分,依次为地区名称、该地区的小麦产量,两部分之间用1个空格1隔开
【输出】
输出有m行,每行为一个小麦产量最高的地区名称（如果有多个,地区名称的输出顺序按输入次序排列）
【输入/输出样例】
【输入】
7
A地区 456
B地区 560
C地区 320
D地区 412
E地区 560
F地区 372
G地区 240
【输出】
B地区
E地区
'''
name=[]
cl=[]
n=int(input())
for i in range(n):
    a=input()
    b=a.split()
    name.append(b[0])
    cl.append(int(b[1]))
for i in range(n):
    if cl[i]==max(cl):
        print(name[i])
    
