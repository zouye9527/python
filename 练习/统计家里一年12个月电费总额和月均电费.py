'''
打开素材文件夹中的python\test4.py，在该文件中编写程序。小王要编写一个程序，
统计家里一年12个月电费总额和月均电费。输入的是12个月每个月的电费，一个数据一行。
输出是电费总额和月均电费，输出结果保留两位小数，且在一行输出，中间以空格分隔。
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
d=[]
for i in range(12):
    d.append(float(input("输入每个月电费%d :"%(i+1))))
s=sum(d)

#获取平均数 
def Get_Average(list):    
    s = 0    
    for item in list:       
        s += item    
    return s/len(list)

average=Get_Average(d)
print("电费总额：%.2f"%s,"月均电费:%.2f"%average)
