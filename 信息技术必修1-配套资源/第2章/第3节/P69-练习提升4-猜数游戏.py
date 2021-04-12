import random
number = 5
secret = random.randint(1, 100)
while number > 0:
    temp1 = int(input("输入一个整数（1-100）："))
    if temp1 == secret:
        print("猜中了！")
        break
    elif temp1 > secret:
        print("数偏大,还是剩", number - 1, "次机会")
    else:
        print("数偏小,还是剩", number - 1, "次机会")
    number -= 1
if number == 0:
    print("答案是", secret)
    print("5次没有猜中，很遗憾，游戏结束")


