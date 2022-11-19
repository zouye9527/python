import turtle
import time
text = turtle.Turtle()
text.hideturtle()
i = 15
while i >= 1:
    text.write(i, font=("黑体", 14, "normal"))
    time.sleep(1)
    text.clear()
    i = i - 1
