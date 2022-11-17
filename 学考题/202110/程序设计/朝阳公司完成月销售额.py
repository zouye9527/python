"""
朝阳公司要对两个子公司的销售业绩进行考评，统计一下两个子公司一年中月销售额的完成情况，年初时对于两个子公司的月销售额任务为50万元，
下列样例是两个子公司每个月的销售记录，其中第一行为子公司A的数据，第二行为子公司B的数据。
请分别统计一年中分别有几个月超额完成了月销售额任务（>50），并输出年销售总额分别为多少。
输入样例
58 29 50 4 75 16 96 12 2 72 56 32
85 37 43 56 69 80 43 8 97 33 56 68
输出样例
5 502
7 675
"""
def xse(s):
    return s>50
gs1=list(map(int,input().split()))
gs2=list(map(int,input().split()))
count1=len(list(filter(xse, gs1)))
count2=len(list(filter(xse, gs2)))
sum1=sum(gs1)
sum2=sum(gs2)
print(count1,sum1)
print(count2,sum2)
