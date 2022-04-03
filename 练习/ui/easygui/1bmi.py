
import easygui
easygui.msgbox(u"你好，我是如花，一个称职的健康助手")
n = easygui.enterbox(u"在测量前我想知道你的姓名")
easygui.msgbox(u"好的"+n+u"我将为你测量你的bmi指数")
easygui.msgbox(u"bmi指数是衡量我们身体的重要指标！！！")
easygui.msgbox(u"bmi的计算方法为：体重除以身高的平方")
tizhong = float(easygui.enterbox(u"请输入你的体重（kg）:"))
shengao = float(easygui.enterbox(u"请输入你的身高（m）:"))
bmi = tizhong/shengao**2
easygui.msgbox(u"你的bmi指数为： %.1f"%bmi)
if bmi<18.5:
                easygui.msgbox(u"您bmi指数为过轻，多吃肉。")
if 18.5<=bmi<=23.9:
                easygui.msgbox(u"你的bmi指数为正常，建议保持")
if 24<=bmi<=26.5:
               easygui.msgbox(u"你的bmi指数为过重，建议控制饮食")
if 27<=bmi<=32:
                easygui.msgbox(u"你的bmi指数为肥胖，建议少吃多运动")
if bmi>32:
                easygui.msgbox(u"你的bmi指数为非常肥胖，建议别吃饭")