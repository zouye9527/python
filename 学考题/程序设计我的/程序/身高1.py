'''
# 12、王老师要对同学们的身高数据进行处理，统计出两个小组中身高为1.68米的同学有几名。
# 输入的第一行为第一小组的身高数据，第二行为第二小组的身高数据，输出数据在一行，中间以空格分隔，
# 第一个数为第一小组身高为1.68米同学人数，第二个数为第二小组身高为1.68米同学人数。
> 输入样例  
> 1.71 1.59 1.72 1.68 1.68 1.82 1.76 1.68 1.89 1.96 1.68 1.74 1.70  
> 1.84 1.58 1.11 1.62 1.25 1.61 1.68 1.65 1.68 1.68 1.66 1.41 1.59 1.58  
> 输出样例  
> 4 3  
'''
a=list(map(float,input('第一小组身高：').split()))
b=list(map(float,input('第二小组身高：').split()))
na=0
nb=0
for i in a:
    if i==1.68:
        na+=1
for i in b:
    if i==1.68:
        nb+=1
print(na,nb)