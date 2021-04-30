import turtle # 导入可以绘制图形的Python内置模块turtle
import time # 导入与时间处理有关的Python内置模块time
text = turtle.Turtle()
text.hideturtle()
#下面代码实现红灯持续15秒，倒计时显示
i = 15
while i >= 1:
    text.color('red','red')
    text.write(i, font=("黑体", 14, "normal"))#显示倒计时数字
    time.sleep(1)#数字显示1秒
    text.clear()#清除数字显示
    i = i - 1
i = ___#请删除横线，填写代码设置绿灯亮15秒
while i >= 1:
    text.color('____','____')#请删除横线，填写代码实现绿灯亮
    text.write(i, font=("黑体", 14, "normal"))
    time.sleep(1)#数字显示1秒
    text.clear()#清除数字显示
    i = i - 1
