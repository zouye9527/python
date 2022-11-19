# 百钱买百鸡问题是一个经典数学问题"鸡翁一，值钱五;鸡母一，值钱三;鸡雏三，值钱一;百钱买百鸡，则翁、母、雏各几何?"
# 小王编写了如下的程序来解决这个问题: 
# A=range(1,101) # ①range
# B={(a,b,c)for a in A for b in A for c in A if a+b+c==100 and 5*a+3*b+c/3==100} # ②逻辑表达式
# print(B)

# 这段代码改造后，可以帮助小王解决很多不定方程问题。
# 例如:有家超市花费1250元购进了单价分别为15元、30元、50元的拖把共计40把，
# 求购进每种拖把的数量。①、②两处应改为(A)

# A.①range(1,41) ②if 15*a+30*b+50*c==1250 and a+b+C==40
# B.①range(1,41) ②if a+b+c==40
# C.①range(1,41) ②if 15*a+30*b+50*c==40 and a+b+c==1250

A=range(1,41) # ①range
B={(a,b,c) for a in A for b in A for c in A if a+b+c==40 and 15*a+30*b+50*c==1250} # ②逻辑表达式
print(B)