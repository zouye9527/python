import math
for A in range(1, 10):
    for B in range (0, 10):
        if A != B:
            k = A * 1000 + A * 100 + B * 10 + B
            c = int(math.sqrt(k)) # 求票据中数字的平方根并取其整数部分
            if c * c == k: # 若k是完全平方数，则找到该票据编号
                print("票据编号是：", k)
