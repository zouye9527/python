'''
【问题描述】
小明周末准备和几个同学去野外郊游,他携带500元到超市采购了若干零食,请编程计算各种零食的花费和剩余的钱数。
【输入】
输入有n+1行,前n行每行有3部分,依次为购买零食的名称、单价、数量,各部分之间用1个空格隔开。第n+1行只有1个—1,表示输入结束
【输出】
输出有n+1行,前n行有两部分,依次为零食的名称和花费的钱数,两部分之间用1个空格隔开,第n+1行是剩余的钱数
【输入/输出样例】
【输入】 
酸奶 2.5 10
巧克力 7 10
面包 5 10
火腿 2 20
薯片 9.5 5
-1
【输出】
酸奶 25.0
巧克力 70.0
面包 50.0
火腿 40.0
薯片 47.5
267.5
'''
name = []
price = [] 
num = []
pay=[]
while True:
    n = input()
    if n == '-1':
        break
    name.append(n.split()[0])
    price.append(float(n.split()[1]))
    num.append(int(n.split()[2]))
for i in range(len(name)):
    pay.append(price[i]*num[i])
for i in range(len(name)):
    print(name[i],pay[i])
print('%.1f'%(500-sum(pay)))