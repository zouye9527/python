import turtle
import time
text=turtle.Turtle()
text.hideturtle()

for i in range(15,0,-1):
    text.write(i,font=("黑体",30,"normal"))
    time.sleep(1)
    text.clear()
    i=i-1
