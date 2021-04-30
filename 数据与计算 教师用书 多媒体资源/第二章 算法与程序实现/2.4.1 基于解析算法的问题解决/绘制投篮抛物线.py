# 分别导入turtle 和math 模块，进行图形绘制和数学运算
import turtle
import math

# 设置物体在初始时刻的坐标值（x0，y0）
x0 = -400
y0 = -100
turtle.penup() # 提起笔移动，不绘制图形
turtle.goto(x0, y0) # 将画笔移动到初始位置x0，y0

# 设置初速度大小v0，与水平方向夹角theta，以及水平方向和垂直方向的初速度v0x、v0y
v0 = 100
theta0 = 60
theta = theta0 / 180 * math.pi
a = -9.8

#水平方向初速度
v0x = v0 * math.cos(theta)
#垂直方向初速度
v0y = v0 * math.sin(theta)


# 通过xt和yt来绘制抛物线：请将下划线去掉补充好相应代码
for t in range(0, 20):
    
    x = x0 + v0x * t #水平方向的位移
    y = y0 + v0y * t + 0.5 * a * t ** 2 #垂直方向的位移
    
    turtle.pendown() # 落下笔移动绘图
    turtle.goto(x, y) # 将画笔移动到坐标xt，yt 位置
    turtle.write((int(x),int(y)),False, align="left") #标注坐标值
