'''
某高校2021年的强基计划体质测试方案中设置了加分项，具体的加分规则如下表：
加分指标评分表

1.男生引体向上评分表(单位:次) 
加分            10   9   8   7   6   5   4   3   2   1
男生测试结果     28  27  26  25  24  23  22  21  20  19

2.女生一分钟仰卧起坐评分表(单位:次) 
加分            10  9   8   7   6   5   4   3   2   1
女生测试结果     68 67  66  65  64  63  62  61  59  57

小王要写一个程序，实现该部分的自动分数统计，程序功能为：输入多名考生考号、测试结果，输出每名考生此单项得分。
输入如下： 
5
001 1 26
002 1 19
003 1 23
004 0 68
005 0 64
其中第一行5，表明有5名考生，下面的每一行数据（如第二行），第一个数“001”是考生的考号，第二个数“1”是性别（1代表男性，0代表女性），
第三个数26是该名男生引体向上测试结果为26个。
输出如下：
001 8
002 1
003 5
004 10
005 6
'''
def male(a):
    maledict={28:10,27:9,26:8,25:7,24:6,23:5,22:4,21:3,20:2,19:1} 
    sc=maledict[a]
    return sc 
def female(a):
    femaledict={68:10,67:9,66:8,65:7,64:6,63:5,62:4,61:3,59:2,57:1} 
    sc=femaledict[a]
    return sc 
n=eval(input()) 
for i in range(0,n): 
    s=input().split() 
    bh=s[0]     # ①
    gender=int(s[1]) # ② 
    cs=int(s[2])     # ③
    if gender==0: 
        score=female(cs)  # ④ 
        print(bh,score) 
    else:
        score=male(cs)    # ⑤
        print(bh,score) 

'''
其中③应该填写（）
A.int(s[2])
B.eval(s[0])
C.n 
'''