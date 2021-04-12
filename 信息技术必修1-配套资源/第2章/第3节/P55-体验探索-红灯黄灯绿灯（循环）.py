import turtle
light = turtle.Turtle()
light.hideturtle()
color = ["red","yellow","green"]
for i in range(3):
    light.penup()
    light.goto(0,-i * 60)
    light.pendown()
    light.color(color[i], color[i])
    light.begin_fill()
    light.circle(20)
    light.end_fill()

