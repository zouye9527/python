while True:
    a = int(input("输入第一个正整数："))
    b = int(input("输入第一个正整数："))
    while b:
        x = a % b
        a = b
        b = x
    print("两个数的最大公约数是：",a)
    c = input("是否继续？（退出程序请输入‘q’或‘Q’；按其它键则继续）")
    if c == "q" or c == "Q":
        break

