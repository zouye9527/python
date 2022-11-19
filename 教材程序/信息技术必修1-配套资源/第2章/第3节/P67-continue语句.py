num = 0
for i in range(1, 5):
    print("进入第", i, "次循环, i=", i)
    if i == 3:
        continue
    num = num + 1
    print("num=", num)
