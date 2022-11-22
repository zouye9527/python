'''
某高校2021年的强基计划体质测试方案中体重指数（BMI）占总分的25％，并订立了相应的评分规则，如下表。
体重指数(BMl)单项计分表(单位:千克/米?)
单项得分            100       80        80         60
男生测试结果    17.3~23.8   <=17.2   23.9~27.3   >=27.4
女生测试结果    17.1~23.3   <=17.0   23.4~25.7   >=25.8
小王要写一个程序，实现本模块的自动计分，程序功能为：输入多名考生考号、身高、体重、性别，输出每名考生此单项得分。
输入如下： 
4
001 1.65 54 0
002 1.78 64 1
003 1.80 78 1
004 1.58 50 0
其中第一行4，表明有4个考生，下面的每一行数据（如第二行），第一个“001”是考生号，“1.65”是身高（单位：米），
“54”是体重（单位：千克），“0”是性别（0表示女生，1表示男生）
注：输入的编号的形式和位数类似于样例，身高和体重有可能是小数
输出如下：
001 100
002 100
003 80
004 100

其中③处应该填写（）
A.s 
B.N 
C.int(s[-1]) 
'''
def malebmi(height,weight): 
    bmi=weight/(height*height) 
    if 17.3<=bmi<=23.8:
        score=100
    if bmi<=17.2 or 23.9<=bmi<=27.3: 
        score=80
    if bmi>=27.4: 
        score=60 
    return score
def femalebmi(height,weight): 
    bmi=weight/(height*height) 
    if 17.1<=bmi<=23.3:
        score=100
    if bmi<=17.0 or 23.4<=bmi<=25.7: 
        score=80
    if bmi>=25.8: 
        score=60 
    return score 
n=eval(input()) 
for i in range(0,n): 
    s=input().split()
    bh=s[0] 
    height=float(s[1]) # ①
    weight=float(s[2]) # ②
    gender=int(s[3])   # ③
    if gender==0: 
        sc=femalebmi(height,weight)  # ④
        print(bh,sc) 
    else:
        sc=malebmi(height,weight)    # ⑤
        print(bh,sc) 


