# 外循环
for i in range(1, 10):
    # 内循环
    for j in range(1, i + 1):
        # 通过end=""设置print()函数不输出换行符
        print(i, " * ", j, " = ", i * j, "\t", end="")
    # 设置换行操作(print()函数不输出任何字符，只进行换行)
    print()





