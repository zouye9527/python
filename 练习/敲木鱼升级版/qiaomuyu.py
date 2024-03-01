import time
import tkinter
import threading
import pygame # pip install pygame
from PIL import Image, ImageTk # pip install pillow

# 准备音频
pygame.mixer.init()
pygame.mixer.music.load('敲.mp3')

# 界面
top=tkinter.Tk()
top.title('敲木鱼加功德')
top.geometry('410x400')
top.configure(bg='black')
# top.overrideredirect(True)
# top.wm_attributes('-transparentcolor', 'black')
# top.attributes('-topmost', 'true')

# 准备图片
qiaomuyutupian=ImageTk.PhotoImage(file='敲木鱼.jpg') # 转化为tkinter可以使用的图片
qiaomuyutupian2=ImageTk.PhotoImage(file='敲木鱼2.jpg') # 转化为tkinter可以使用的图片

# 初始化功德
gongde=0

# 标签
label1=tkinter.Label(top,text='积攒功德：'+str(gongde),font=('华文新魏',15),fg='white',bg='black',width=18)
label1.place(x=100,y=70)

def showplus():
	global gongde
	for i in range(4):
		text1.insert('insert',' \n')
	else:
		text1.insert('insert',' 功德 + 1')

	for i in range(5):
		time.sleep(0.04)
		text1.delete(1.0, 2.0)

	gongde=gongde+1
	label1.config(text='积攒功德：'+str(gongde))

def changetupian():
	button1.config(image=qiaomuyutupian2)
	time.sleep(0.1)
	button1.config(image=qiaomuyutupian)

# 方法
def qiaomuyu():
	# 多线程启动解决延时，虽然延迟足够小，但为了更有效果
	th=threading.Thread(target=pygame.mixer.music.play)
	th.start()

	th2=threading.Thread(target=showplus)
	th2.start()

	th3=threading.Thread(target=changetupian)
	th3.start()

# 按钮
button1=tkinter.Button(top,image=qiaomuyutupian,relief='ridge',command=qiaomuyu)
button1.place(x=100,y=100)

text1=tkinter.Text(top,width=10,height=5,bg='black',bd=0,foreground='white')
text1.place(x=125,y=115)


top.mainloop()