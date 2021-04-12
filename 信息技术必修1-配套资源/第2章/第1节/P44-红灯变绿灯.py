import turtle # 导入可以绘制图形的Python内置模块turtle
import time # 导入与时间处理有关的Python内置模块time
#初始化红绿灯
light = turtle.Turtle()
light.hideturtle()
light.screen.delay(0) # 禁用绘制过程的动画显示
# 红灯亮
light.color("red", "red")
light.begin_fill()
light.circle(20)
light.end_fill()
# 红灯保持显示
time.sleep(15)
# 绿灯亮
light.color("green", "green")
light.begin_fill()
light.circle(20)
light.end_fill()
