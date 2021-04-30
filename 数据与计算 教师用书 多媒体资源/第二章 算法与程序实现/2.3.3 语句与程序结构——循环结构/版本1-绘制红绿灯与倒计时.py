#导入模块
import time
import turtle
import sinomaps

# 设置禁行灯为红色、灰色，变量名为stopColors
stopColors = ['red', 'grey']
# 设置通行灯为灰色、绿色，变量名为goColors
goColors = ['grey', 'green']

# 初始化界面
#生成一个sinomaps模块的对象light
light = sinomaps.RGLight()
#绘制禁行灯
light.draw_lights(stopColors)
#绘制按钮
light.draw_button()
# 初始状态为禁止通行
light.state = sinomaps.LightStatus.Stop

while True:
    # 按钮可以使用
    light.buttonEnabled = True
    
    # 按钮被按下
    if light.state == sinomaps.LightStatus.ButtonClicked:
        # 按钮不可以使用
        light.buttonEnabled = False

        #红灯等待5秒
        for i in range(___,_____,____):
            #绘制禁行灯
            light.draw_lights(_____________)
            #输出倒计时，参数1是代表倒计时数字的变量名，参数2是颜色：红色
            light.write_seconds(______, _________)
            #持续1秒
            time.sleep(___)
            #清除倒计时
            light.clear_seconds()

        #绿灯等待5秒
        for j in range(___,_____,____):
            #绘制通行灯
            light.draw_lights(_____________)
            #输出倒计时，参数1是代表倒计时数字的变量名，参数2是颜色：绿色
            light.write_seconds(______, _________)
            #持续1秒
            time.sleep(___)
            #清除倒计时
            light.clear_seconds()
        
        
        # 终止界面
        # 绘制禁行灯
        light.draw_lights(stopColors)
        #绘制按钮
        light.draw_button()
        # 终止状态为禁止通行
        light.state = sinomaps.LightStatus.Stop
        
    #刷新界面，保持程序正常运行    
    light.waiting()    
        
        


