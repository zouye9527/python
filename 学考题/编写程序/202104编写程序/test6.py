"""
打开素材文件夹中的python\test6.py，在该文件中编写程序。
康欣公司，要统计分公司的销售额总和和销售额的最大值和最小值，请编写程序完成此项工作。
输入的数据是10个子公司的销售额（都为整数，且销售额的范围在100到100000之间），一行一个数据，
在一行中输出销售额的总和、最大值和最小值，中间以空格分隔。
输入样例：
7942 
80541 
155 
86428 
2673 
20555 
56505 
87105 
18250 
48707 
输出样例：
408861 87105 155
"""
d=[]
for i in range(10):
    d.append(int(input())) 
print(sum(d),max(d),min(d))
