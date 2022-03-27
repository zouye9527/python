#heads为头的个数，feet为脚的个数, c为鸡的个数， r为兔的个数
heads = 8
feet = 26
for c in range(1, heads):
    r = heads-c
    if 2*c+4*r == feet:
        print("鸡有" ,c, "只，兔有" ,r, "只。")