'''
小王要编写一个程序，统计家里一年12个月电费总额和月均电费。输入的是12个月每个月的电费，一个数据一行。输出是电费总额和月均电费，输出结果保留两位小数，且在一行输出，中间以空格分隔。
输入样例：
42.10
27.40
62.83
39.33
88.99
19.41
59.82
40.07
42.63
13.36
47.22
45.70
输出样例：
528.86 44.07
'''
df=[]
for i in range(1,13):
    n=float(input("请输入%d月的电费："%i))
    df.append(n)
print("年度电费总额和月均电费分别是：%.2f %.2f"%(sum(df),(sum(df)/12)))