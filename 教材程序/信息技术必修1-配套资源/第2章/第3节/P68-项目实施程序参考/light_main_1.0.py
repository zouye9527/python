import sinomaps
import time
import turtle
# 设置红绿灯停止和通行状态的颜色
stopColors = ['red', 'grey']
goColors = ['grey', 'green']

# 初始化界面（红绿灯）
light = sinomaps.RGLight()
light.draw_lights(stopColors)
light.draw_button()
# 设初始值为停止
light.state = sinomaps.LightStatus.Stop

while True:
    # 打开按钮
    light.buttonEnabled = True
    # 判断是否按下按钮
    if light.state == sinomaps.LightStatus.ButtonClicked:
        # 关闭按钮
        light.buttonEnabled = False
        #红灯等待15秒
        for i in range(15,0,-1):
            time.sleep(1)
            light.draw_lights(stopColors)
            light.write_seconds(i, 'red')
        #绿灯等待20秒
        for j in range(20,0,-1):
            time.sleep(1)
            light.draw_lights(goColors)
            light.write_seconds(j, 'green')
        
        #红灯亮
        time.sleep(1)
        light.draw_lights(stopColors)
        #重置状态
        light.draw_button()
        light.state = sinomaps.LightStatus.Stop
        #锁定按钮60秒
        time.sleep(60)
    light.waiting()
        
        


