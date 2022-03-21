"""
王老师要对两个小组的数学成绩进行对比，分别计算出两个小组及格率（及格为成绩≥60）的差异。输入的第一行为第一小组每个人的成绩，
第二行为第二小组每个人的成绩，在一行中输出两个小组的及格率分别为多少，输出结果保留一位小数。
输入样例
50 4 75 16 96 12 2 72 56 32
43 56 69 80 43 8 97 33 56 68
输出样例
30.0% 40.0%
"""
def jg(n):
    return n>=60
xz1=list(map(int,input().split()))
xz2=list(map(int,input().split()))
count1=len(xz1)
count2=len(xz2)
jg1=len(list(filter(jg, xz1)))
jg2=len(list(filter(jg, xz2)))
jgl1=jg1/count1
jgl2=jg2/count2
print("%.1f%%"%(jgl1*100),"%.1f%%"%(jgl2*100))
