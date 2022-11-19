import turtle
import time
import tkinter
from enum import Enum


class LightStatus(Enum):
    Stop = 0
    ButtonClicked = 1
    Wait = 2
    Go = 3
    Warn = 4


class RGLight:
    light = turtle.Turtle()
    secondLight = turtle.Turtle()
    button = turtle.Turtle()
    window = turtle.Screen()
    window.bgpic('bg.gif')
    second = 0
    state = LightStatus.Stop
    _last_second = 0
    buttonEnabled = True

    running = True

    def __init__(self):
        self.light.up()
        self.secondLight.up()
        self.button.up()
        self.light.shape('circle')
        self.light.shapesize(1, 1, 1)
        self.light.hideturtle()
        self.secondLight.hideturtle()
        self.button.hideturtle()
        self.window.tracer(0, 0)

    def _draw_rect(self, t, center_x, center_y, width, height, fillcolor='transparent'):
        t.up()
        t.goto(center_x, center_y)
        if fillcolor != 'transparent':
            t.pencolor(fillcolor)
            t.fillcolor(fillcolor)
            t.begin_fill()
        t.setheading(0)
        t.forward(width / 2)
        t.setheading(270)
        t.down()
        t.forward(height / 2)
        t.setheading(180)
        t.forward(width)
        t.setheading(90)
        t.forward(height)
        t.setheading(0)
        t.forward(width)
        t.setheading(270)
        t.forward(height / 2)
        if fillcolor != 'transparent':
            t.end_fill()
        t.up()

    def draw_lights(self, colors):
        try:
            self.light.clear()
            self.light.goto(0, 150)
            self.light.color('#000000')
            self.light.write('模拟自助式人行过街红绿灯', align='center', font=('Microsoft Yahei', 20, 'normal'))
            self._draw_rect(self.light, 0, 55, 30, 60, '#000000')
            x = 0
            y = 70
            for color in colors:
                self.light.up()
                self.light.goto(x, y)
                self.light.pencolor(color)
                self.light.fillcolor(color)
                self.light.stamp()
                y = y - 25
        except tkinter.TclError:
            self.running = False

    def draw_button(self):
        self._draw_rect(self.button, 95, -100, 30, 30, '#666666')
        self.button.color('#000000')
        self.button.goto(95, -110)
        self.button.write('按', align='center', font=('Microsoft Yahei', 10, 'normal'))
        self.window.onclick(self._button_click)

    def _button_click(self, x, y):
        if not self.buttonEnabled:
            return
        if (x < 85 and y < -110) or (x < 85 and y >-90) or (x > 105 and y < -110) or (x > 105 and y > -85):
            return
        self._last_second = time.time()
        self.state = LightStatus.ButtonClicked

    def clear_seconds(self):
        try:
            self.secondLight.clear()
        except tkinter.TclError:
            self.running = False

    def write_seconds(self, second, color):
        try:
            self.secondLight.clear()
            self._draw_rect(self.secondLight, 0, 0, 30, 30, '#777777')
            self.secondLight.goto(0, -10)
            self.secondLight.color(color)
            self.secondLight.write(str(second).zfill(2), align='center', font=("DS-Digital", 15, "bold"))
        except tkinter.TclError:
            self.running = False

    def waiting(self):
        try:
            now = time.time()
            if (self.state == LightStatus.Wait
                or self.state == LightStatus.Go
                or self.state == LightStatus.Warn)\
                    and self.second > 0 and now - self._last_second >= 1:
                self._last_second = now
                self.second = self.second - 1
            time.sleep(0.1)
            self.window.update()
        except turtle.Terminator:
            self.running = False
        except tkinter.TclError:
            self.running = False
