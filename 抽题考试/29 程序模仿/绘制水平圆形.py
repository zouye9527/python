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
小王使用Python编写了下面的代码,完成了图形1的绘制。图形1中四个圆相切,半径都为10,左侧第一个圆的圆心坐标为(0,10)。
图形2中,圆的半径仍然为10,左侧第一个圆的圆心坐标也为(0,10),无论图形1还是图形2,四个圆的圆心都在经过左侧第一个圆的圆心的水平直线上,
以下哪个修改可以实现图形2的绘制（ ）

'''
'''
A．修改语句4,修改为for x in [0,20+r,30+r,40+r]: 
B．修改语句4,修改为for x in [0,20-r,40-r,60-r]: 
C．修改语句4,修改为for x in [0,r,2*r,3*r]:

'''
import turtle as t 
t.pencolor('red') 
r=10
for x in [0,r,2*r,3*r]: 
    t.penup()
    t.goto(x,0) 
    t.pendown() 
    t.circle(r) 
t.done()
