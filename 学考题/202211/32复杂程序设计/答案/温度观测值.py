'''
输入某天温度观测的次数和每次的观测值，统计高于观测值平均值的次数。
输入
8 
11 
12 
11 
7 
7 
7 
5 
4 
注：输入共n n+1行（n＜＝24），第一行为一个整数，为观测次数；接下来的n行，每行一个整数，为每次的观测值
输出
3
注：输出一个整数，表明高于观测值平均值的次数
'''
n=int(input())
s0=[]
m=0
for i in range(n):
    s0.append(int(input()))
avg=sum(s0)/n
for i in range(n):
    if s0[i]>avg:
        m+=1
print(m)



