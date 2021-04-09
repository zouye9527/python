import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("方程无解")
    elif delta == 0:
        s = -b / (2 * a)
        print("两根相等：x=",s)
    else :
        root = math.sqrt(delta)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)
        print("x1=", x1, "\t", "x2=", x2)

