from turtle import *
def up():
    setheading(90)
    fd(50)
def down():
    setheading(-90)
    fd(50)
def right():
    setheading(0)
    fd(50)
def left():
    setheading(180)
    fd(50)
onkey(up,'w')#onkey函数一个参数为要实现的函数名，另一个参数为对应键
onkey(down,'s')
onkey(right,"d")
onkey(left,"a")
listen()#turtle.listen()监听键盘









mainloop()#防止闪退


