# import turtle as t 
# t.pencolor('red') 
# r=10
# for y in range (0, 2): 
#     for x in [0, 20]: 
#         t.penup()
#         t.goto(x+2*y*r,-2*y*r) 
#         t.pendown()
#         t.circle(r)
# t.done
'''
 小王使用Python编写了下面的代码，完成了图形1的绘制。图形1中四个圆半径都为10，左上角圆的圆心坐标为(0，10)。
 图形2中，圆的半径仍然为10，左上角圆的圆心坐标为(0，10)，以下哪个修改可以实现图形2的绘制（ ）
'''
import turtle as t 
t.pencolor('red') 
r=10
for y in range (0, 4): 
    for x in [0, 20]: 
        t.penup()
        t.goto(x+2*y*r,-2*y*r) 
        t.pendown()
        t.circle(r)
t.done
'''
A．修改语句9，修改为t.circle(4*r)
B．修改语句4，修改为for y in range(0,4):
C．修改语句4，修改为for y in range(0,8):

'''