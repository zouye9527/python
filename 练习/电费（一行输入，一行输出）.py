'''
小王要编写一个程序，统计家里一年12个月电费总额和月均电费。在一行输入每个月的电费，中间以空格分隔。输出结果为电费总额和月均电费，输出结果保留两位小数，在一行输出，中间以空格分隔。
输入样例：
42.10 27.40 62.83 39.33 88.99 19.41 59.82 40.07 42.63 13.36 47.22 45.70
输出样例：
528.86 44.07
'''
df=[]
df2=[]
n=input("请输入12个月的电费，用空格隔开：")
df=n.split()
for i in df:
    df2.append(float(i))
print("12个月的电费总额、月均电费分别是：%.2f %.2f"%(sum(df2),sum(df2)/12))