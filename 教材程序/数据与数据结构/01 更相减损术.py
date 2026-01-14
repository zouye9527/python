# 更相减损术求最大公约数
def gcd(a, b):
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
# 测试
num1 = int(input("请输入第一个正整数: "))
num2 = int(input("请输入第二个正整数: "))
result = gcd(num1, num2)
print(f"最大公约数是: {result}")
# 输出: 最大公约数是: 6
