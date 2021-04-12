try:
    h = eval(input("输入高度"))
    if 0 <= h <= 1500:
        t = 22 - h / 100 * 0.5
        print("此处的气温为：",round(t, 1))
    else:
         print("输入数据超出范围！")
except:
    print("输入数据格式有误！")

