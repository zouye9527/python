import math
n = int(input("请输入正多边形的边数："))
i = 6
x = 1
s = 6 * math.sqrt(3) / 4
while i <= n / 2:
    h = math.sqrt (1 - (x / 2) ** 2)
    s = s + i * x * (1 - h) / 2
    x = math.sqrt((x / 2) ** 2 + (1 - h) ** 2)
    i = 2 * i
print("当正多边形的边数为", n, "时,π的近似值为:", s)
