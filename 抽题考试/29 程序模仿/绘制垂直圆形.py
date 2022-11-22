# import turtle as t 
# t.pencolor('red') 
# r=10
# for x in [0,20,40,60]: 
#     t.penup()
#     t.goto(x,0) 
#     t.pendown() 
#     t.circle(r) 
# t.done()

'''
小王使用Python编写了下面的代码，完成了图形1的绘制。
图形1中四个圆相切，半径都为10，左侧第一个圆的圆心坐标为(0，10)，四个圆的圆心在经过(0，10)的水平直线上。
图形2中，圆的半径仍然为10，最下端圆的圆心坐标为(0，10)，四个圆相切，四个圆的圆心在经过(0，10)的垂直直线上。
以下哪个修改可以实现图形2的绘制（ ）
'''
'''
A.修改语句4,修改为for x in [0, 20, 30, 40]: 
B.修改语句6,修改为t.goto(0, x) 
C.修改语句6,修改为t.goto(0, 0)

'''
import turtle as t 
t.pencolor('red') 
r=10
for x in [0,20,40,60]: 
    t.penup()
    t.goto(0,x) 
    t.pendown() 
    t.circle(r) 
t.done()