# "老师拿了a元去买书,买了b套故事书,每套c元,编程计算还剩多少元。"
# 输入
# 70.5
# 7
# 9.5
# "注:输入分为三行,第一行是浮点数为a,第二行是整数为b,第三行是浮点数为c"
# 输出
# 4.00
# 注:输出结果保留两位小数
a=float(input())
b=int(input())
c=float(input())
d=a-b*c
print("%.2f"%d)
