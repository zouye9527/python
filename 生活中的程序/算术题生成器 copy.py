# 输入n,表示算术题的最小数；输入m,表示算术题的最大值;s表示答案的最大值,答案范围1<=ans<=s
n = int(input("题目的最小数:"))
m = int(input("题目的最大数:"))
s = int(input("答案最大值:"))
K=0
for i in range(n, m + 1):
    for j in range(n, m + 1):
        if i + j <= s:
            print(i, "+", j, "=")
            K+=1
        if i-j>0:
            print(i, "-", j, "=")
            K+=1
        if j-i>0:
            print(j, "-", i, "=")
            K+=1
print("生成了%d道题"%K)
