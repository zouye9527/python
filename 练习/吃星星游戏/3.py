import turtle
import random

# 设置屏幕
screen = turtle.Screen()
screen.title("吃星星游戏")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# 创建玩家乌龟
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.speed(0)

# 创建星星
star = turtle.Turtle()
star.shape("circle")
star.color("yellow")
star.penup()
star.speed(0)
x = random.randint(-290, 290)
y = random.randint(-290, 290)
star.goto(x, y)

# 分数
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-290, 260)
score_display.color("white")
score_display.write("Score: {}".format(score), align="left", font=("Arial", 16, "normal"))

# 移动函数
def move_up():
    y = player.ycor()
    y += 20
    if y > 290:
        y = 290
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    if y < -290:
        y = -290
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        x = 290
    player.setx(x)

# 键盘绑定
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# 主循环
while True:
    if player.distance(star) < 20:
        star.hideturtle()
        score += 1
        score_display.clear()
        score_display.write("Victory! Score: {}".format(score), align="center", font=("Arial", 16, "normal"))
        break
    
    screen.update()

# 等待用户关闭窗口
screen.mainloop()
