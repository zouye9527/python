"""
小王要编写一个程序，统计家里一年12个月电费总额和月均电费。
在一行输入每个月的电费，中间以空格分隔。输出结果保留两位小数，
且在两行输出，第一行为电费总额，第二行为月均电费
输入样例：
42.10 27.40 62.83 39.33 88.99 19.41 59.82 40.07 42.63 13.36 47.22 45.70
输出样例：
528.86 
44.07
"""
peplist=list(map(float,input("请横向输入每个月的电费，中间用空格隔开：").split()))
s=sum(peplist)
aver=s/len(peplist)
print("电费总额：%.2f"%s)
print("月均电费%.2f"%aver)
