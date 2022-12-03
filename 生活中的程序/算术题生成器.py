# 输入n,表示算术题的最小数；输入m,表示算术题的最大值;s表示答案的最大值,答案范围1<=答案<=s
# 输入要生成的题目数量，随机抽题并输出
import random

ss=[]
n = int(input("题目的最小数:"))
m = int(input("题目的最大数:"))
s = int(input("答案最大值:"))
for i in range(n, m + 1):
    for j in range(n, m + 1):
        if i + j <= s:
            ss.append(str(i)+"+"+str(j)+'=')
        if i-j>=0:
            ss.append(str(i)+"-"+str(j)+'=')
        if j-i>=0:
            ss.append(str(j)+"-"+str(i)+'=')
k=s**2-2
p=int(input("请输入要生成的题的数量(不能超过%d):"%k))
if p<=k:
    result=random.sample(range(1,k),p)
    for i in result:
        print(ss[i+1])
else:
    print("数量超过了最大值")
