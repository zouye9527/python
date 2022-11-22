'''
甲乙两地相距b千米，小陈从甲地出发，若想在a小时内到达乙地，求他骑行的最低速度是每小时多少千米
输入输出说明：
 1、输入有2行，每行有1个数；第1行中的数是a的值，第2行中的数是b的值 
 2、输出有1行，为程序计算的结果（保留两位小数）；
 如果输入中的a≤0，则输出“输入错误” 
 输入输出样例：
 样例1：
 输入： 
 9 
 18 
 输出： 
 2.00 
 样例2：
 输入： 
 0 
 18 
 输出
 输入错误
'''
a=float(input())
b=float(input())
if a<=0:
    print("输入错误")
else:
    v=b/a
    print("%.2f"%v)