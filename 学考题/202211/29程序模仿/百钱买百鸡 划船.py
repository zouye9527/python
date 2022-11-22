'''
下图的程序一可以解决百钱买百鸡问题:鸡翁一，值钱五;鸡母一，值钱三鸡雏三，值钱一;百钱买百鸡，则翁、母、雏各几何?
分析可知，鸡翁最多20只，鸡母最多33只，鸡雏最多100只。
于是对程序一进行优化，减少枚举的次数，得到了下图中的程序二。 
程序一：
A=range(1,101)
B={(a,b,c)for a in A for b in A for c in A if a+b+c==100 and 5*a+3*b+c/3==100}
print(B)

程序二：
A=range(1,21)
A1=range(1,34)
A2=range(1,101)
B={(a,b,c)for a in A for b in A1 for c in A2 if a+b+c==100 and 5*a+3*b+c/3==100}
print(B)

仿照上面程序二的思想解决乘船问题:
三年级2班共48人到公园划船，如果每只小船可坐3人，每只大船可坐5人。那么需要小船和大船各几只。下 
程序中①、②两处应填写() 
A.①range(1,17) ②range(1,10)
B.①range(1,10) ②range(1,17)
C.①range(1,49) ②range(1,10)
'''
A=range(1,17)      # ①
A1=range(1,10)     # ②
B={(a,b) for a in A for b in A1 if 3*a+5*b==48}
print(B)


