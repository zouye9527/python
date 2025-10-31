'''
打开Python文件夹中的test3.py文件,在其中编写程序解决如下问题
【问题描述】
小李的妈妈开着一家服装店,由于数据更新不及时,
所以年底盘货时发现有几款衣服的账面库存与实际库存不符，
请编写程序找出所有账面库存与实际库存数量不符的衣服款式编号
【输入】
输入有3行,第1行为衣服款式编号,
第2行为账面库存数量,第3行为实际库存数量,
每行包含10部分,各部分之间分别用1个空格隔开
【输出】
输出有n行,每行为一个账面库存与实际库存数量不符的衣服款式编号
（输出顺序按输入次序排列）
【输入/输出样例】
【输入】
a b c d e f g h i j
8 3 7 5 7 9 1 3 5 2
7 6 3 5 5 7 2 3 4 3
【输出】
a
b
c
e
f
g
i
j
'''

style_numbers = input().split()
accounted_stock = list(map(int, input().split()))
actual_stock = list(map(int, input().split()))
for i in range(10):
    if accounted_stock[i] != actual_stock[i]:
        print(style_numbers[i])
