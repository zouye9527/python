import easygui as g
ls=g.multchoicebox(msg="请选择购买的商品",title="",choices=('1.matebook13s:2000','2.无线耳机:150','3.蓝牙鼠标:30','4.鼠标垫:10','5.双肩包:80'))
print(ls)
g.msgbox(ls)