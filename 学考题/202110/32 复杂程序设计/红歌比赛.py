"""
学校要进行红歌比赛，需要计算每个班的最终得分。计分规则如下：去掉一个最高分和一个最低分，余下分数的平均分即为该班的最后得分。
请编写程序，程序功能如下：逐一输入评委打分（评委个数大于等于7个，小于20个，
输入的分数在60-100之间，包括60，但不包括100），输出平均分，保留一位小数。
输入：
74 86 79 71 86 92 61 86 90 95
输出：
83.0
"""
sc0=input().split()
sc=[]
for i in range(len(sc0)):
    sc.append(float(sc0[i]))
avg=(sum(sc)-max(sc)-min(sc))/(len(sc)-2)
print("%.1f"%avg)
