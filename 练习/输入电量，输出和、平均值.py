'''
打开素材文件夹中的python\test5.py，在该文件中编写程序。
小王要编写一个程序，统计家里一年12个月电费总额和月均电费。
在一行输入每个月的电费，中间以空格分隔。输出结果保留两位小数，
且在两行输出，第一行为电费总额，第二行为月均电费
输入样例：
42.10 27.40 62.83 39.33 88.99 19.41 59.82 40.07 42.63 13.36 47.22 45.70
输出样例：
528.86 
44.07
'''

df=[]
s=input("请输入12个月电量，用空格隔开：")
df=s.split(" ")
print(df)
df2={}
for i in range(0,len(df)):
    df2[i]=float(df[i])
print(df2)

def summ(list):    
    s0 = 0    
    for item in list:       
        s0 += item    
    return s0

s1=summ(df2)
aver=s1/12

print(float(s1))
print(float(aver))
