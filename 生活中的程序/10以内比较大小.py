import random
a=range(1,11)
n=int(input("输入要生成的比较大小题目的数量："))
for i in range(n):
    print(random.choice(a)," ",random.choice(a))
