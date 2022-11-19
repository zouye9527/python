n = int(input("请输入乘坐的站点数:"))
if n <= 5:
    print("票价2元")
elif n <= 10:
    print("票价3元")
elif n <= 16:
    print("票价4元")
else:
    print("票价5元")
