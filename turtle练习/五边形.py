import turtle
n=int(input("请输入正多边形的边数："))
t=turtle.Turtle()

t.penup()
t.goto(0,300)
t.pendown()

r=180-(n-2)*180/n
for i in range(n):
    t.forward(50)
    t.right(r)
turtle.done()