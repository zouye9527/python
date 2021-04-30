
weight = eval(input("请输入你的体重（kg）："))

step = eval(input("请输入你的步数："))

# 请将下划线去掉补充好相应代码

stepLength = 0.6 #设置“步长”

k = 0.8214 #设置“系数k”

calorie = weight * step * stepLength * k / 1000 #计算热量

print("你消耗的热量为", calorie, " kcal。")
