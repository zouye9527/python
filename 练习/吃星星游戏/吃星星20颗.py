import turtle
import random
import tkinter as tk
from tkinter import messagebox

# 设置屏幕
screen = turtle.Screen()
screen.title("吃星星游戏")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# 创建玩家（小乌龟）
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()
player.speed(0)
player.goto(0, 0)

# 创建星星列表
stars = []
for _ in range(20):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("yellow")
    star.penup()
    star.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    star.goto(x, y)
    stars.append(star)

# 分数
score = 0

# 移动函数
def move_up():
    y = player.ycor()
    y += 20
    if y > 290:
        game_over("游戏结束")
        return
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= 20
    if y < -290:
        game_over("游戏结束")
        return
    player.sety(y)

def move_left():
    x = player.xcor()
    x -= 20
    if x < -290:
        game_over("游戏结束")
        return
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 290:
        game_over("游戏结束")
        return
    player.setx(x)

# 游戏结束函数
def game_over(message):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("游戏结束", message)
    screen.bye()

# 键盘绑定
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# 主循环
while True:
    for star in stars:
        if player.distance(star) < 20:
            star.hideturtle()
            stars.remove(star)
            score += 1
            if score == 20:
                game_over("恭喜你，游戏胜利")
    screen.update()
