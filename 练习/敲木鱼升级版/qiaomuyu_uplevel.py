import time
import tkinter
from tkinter import messagebox
import threading
import pygame # pip install pygame
from PIL import Image, ImageTk # pip install pillow

class window(tkinter.Tk):
	def __init__(self):
		super().__init__()

		# 初始化功德
		self.gongde=0

		# 准备音频
		self.pygame=pygame
		self.pygame.mixer.init()
		self.pygame.mixer.music.load('敲.mp3')

		# 准备图片
		self.qiaomuyutupian=ImageTk.PhotoImage(file='敲木鱼.jpg') # 转化为tkinter可以使用的图片
		self.qiaomuyutupian2=ImageTk.PhotoImage(file='敲木鱼2.jpg') # 转化为tkinter可以使用的图片

		# 启动界面
		self.base_top()

	def base_top(self):
		self.title('敲木鱼加功德')
		self.geometry('410x400')
		self.configure(bg='black')

		# 标签
		self.label1=tkinter.Label(self,text='积攒功德：'+str(self.gongde),font=('华文新魏',15),fg='white',bg='black',width=18)
		self.label1.place(x=100,y=70)

		# 按钮
		self.button1=tkinter.Button(self,image=self.qiaomuyutupian,relief='ridge',command=self.qiaomuyu)
		self.button1.place(x=100,y=100)

		# 按钮
		self.button2=tkinter.Button(self,text='互动',width=10,command=self.thread_hudong)
		self.button2.place(x=160,y=315)

		# 消息
		self.text1=tkinter.Text(self,width=10,height=5,bg='black',bd=0,foreground='white')
		self.text1.place(x=125,y=115)

	def showplus(self):
		# 文字浮动
		for i in range(4):
			self.text1.insert('insert',' \n')
		else:
			self.text1.insert('insert',' 功德 + 1')
		for i in range(5):
			time.sleep(0.04)
			self.text1.delete(1.0, 2.0)

		# 功德+1
		self.gongde=self.gongde+1
		self.label1.config(text='积攒功德：'+str(self.gongde))

	def changetupian(self):
		self.button1.config(image=self.qiaomuyutupian2)
		time.sleep(0.1)
		self.button1.config(image=self.qiaomuyutupian)

	def qiaomuyu(self):
		# 多线程启动解决延时，虽然延迟足够小，但为了更有效果
		th=threading.Thread(target=self.pygame.mixer.music.play)
		th.start()

		th2=threading.Thread(target=self.showplus)
		th2.start()

		th3=threading.Thread(target=self.changetupian)
		th3.start()

	def thread_hudong(self):
		th4=threading.Thread(target=self.hudong)
		th4.start()

		self.frame=tkinter.Frame(self,width=200,height=40,bg='white')
		self.frame.place(x=103,y=350)

		self.label2=tkinter.Label(self.frame,text='正在摄像头中，请稍等...',bg='white')
		self.label2.place(x=33,y=10)

	def hudong(self):
		import cv2
		import mediapipe as mp

		mp_hands = mp.solutions.hands
		hands = mp_hands.Hands()
		mp_drawing = mp.solutions.drawing_utils

		# coding:utf-8`
		cap = cv2.VideoCapture(0)  # 打开摄像头
		mark_one=0
		while True:
			self.frame.destroy()

			ret, frame = cap.read()  # 读取视频帧
			if not ret:
				break
			image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换颜色空间
			results = hands.process(image)  # 手势识别

			# 处理识别结果
			if results.multi_hand_landmarks:
				for hand_landmarks in results.multi_hand_landmarks:
					mp_drawing.draw_landmarks(
						frame,
						hand_landmarks,
						mp_hands.HAND_CONNECTIONS) # 用于指定地标如何在图中连接。

					for point in hand_landmarks.landmark:
						x = int(point.x * frame.shape[1])
						y = int(point.y * frame.shape[0])
						if y < 200:
							mark_one=1
						if y > 400:
							if 1 - mark_one == 0:
								self.qiaomuyu()
								mark_one=0

						cv2.circle(frame, (x, y), 5, (0, 255, 0), -1) # 画出关键点

			cv2.imshow('Gesture Recognition', frame)  # 显示结果
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()

if __name__ == '__main__':
	top=window()
	top.mainloop()