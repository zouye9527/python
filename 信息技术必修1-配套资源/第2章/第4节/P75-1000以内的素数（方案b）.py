import math      #导入math模块，以便使用其中的数学函数
k = True
for n in range(2, 1000):
    m = int(math.sqrt(n))  #函数sqrt()用于求平方根
    for j in range(2, m + 1):
        if n % j == 0:
            k = False
            break
    if k:
        print(n)
    k = True

