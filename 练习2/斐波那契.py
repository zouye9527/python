# 程序功能：计算斐波那契数列的前n项
def fibonacci(n):
    fib_list = []
    a, b = 1, 1
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b  # 斐波那契数列递推公式
    return fib_list
# 测试程序
n = int(input("请输入要计算的项数："))
if n <= 0:
    print("请输入正整数！")
else:
    result = fibonacci(n)
print(f"斐波那契数列前{n}项为：{result}")
#（1）程序中变量n的数据类型是①（整型）。
#（2）斐波那契数列的递推关系体现在代码行：②（a,b=b,a+b）。
#（3）该程序使用的基本算法结构是③（循环）结构。
#（4）函数fibonacci(n)的返回值类型是④（列表）。
#（5）如果输入n=5，程序输出结果为：⑤（1,1,2,3,5）。
