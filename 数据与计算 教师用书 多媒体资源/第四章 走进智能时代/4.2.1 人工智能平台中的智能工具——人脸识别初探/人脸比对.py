# -*- coding: utf-8 -*-
# 
from aip import AipFace
import cv2
import base64
import sys
sys.setrecursionlimit(1000000) 
from graphics import*
import tkinter as tk
from tkinter import filedialog
from time import sleep

APP_ID = '16290061'
API_KEY = '4uKwGeC2Ci7aHbn6dHuYIrGc'
SECRET_KEY = 'KRdPZdtYwLsdEthIGu03jb7GEeRtTUMF'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

filepath1 = "C:\\Users\\lenovo\\Desktop\\face\\752\\shl1.jpg"
filepath2 = "C:\\Users\\lenovo\\Desktop\\face\\752\\shl2.jpg"
win = GraphWin('人脸比对第1张图片', 500, 90)
win.setBackground("yellow")
Text(Point(win.getWidth()/2, 40), "请在文件夹中选择 第1张 人脸图片").draw(win)
sleep(1)
root = tk.Tk()
root.withdraw()
filepath1 = filedialog.askopenfilename()

win = GraphWin('人脸比对第2张图片', 500, 90)
win.setBackground("yellow")
Text(Point(win.getWidth()/2, 40), "请在文件夹中选择 第2张 人脸图片").draw(win)
sleep(1)
root = tk.Tk()
root.withdraw()
filepath2 = filedialog.askopenfilename()

with open(filepath1, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')
imageType = "BASE64"

options = {
    'max_face_num': 1, 
    'face_fields': "expression,faceshape",
}		
		
result1 = aipFace.detect(image, imageType,options)

location1=result1['result']['face_list'][0]['location']
left_top1=(int(location1['left']),int(location1['top']))
right_bottom1=(int(left_top1[0]+location1['width']),int(left_top1[1]+location1['height']))
 
img1=cv2.imread(filepath1)
cv2.rectangle(img1,left_top1,right_bottom1,(0,255,0),2)
cv2.imshow('img1',img1)

with open(filepath2, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')
imageType = "BASE64"

	
result2 = aipFace.detect(image, imageType,options)

location2=result2['result']['face_list'][0]['location']
left_top2=(int(location2['left']),int(location2['top']))
right_bottom2=(int(left_top2[0]+location2['width']),int(left_top2[1]+location2['height']))
 
img2=cv2.imread(filepath2)
cv2.rectangle(img2,left_top2,right_bottom2,(0,255,0),2)
cv2.imshow('img2',img2)		
				
	
result = aipFace.match([
    {
        'image' : base64.b64encode(open(filepath1, 'rb').read()).decode(),
        'image_type': 'BASE64',
    },
    {
       'image' : base64.b64encode(open(filepath2, 'rb').read()).decode(),
        'image_type': 'BASE64',
    }
])

res=result['result']['score']

if res>80:
	#print ("图1和图2是同一个人.\n")
	win = GraphWin('检测结果', 300, 300)
	Text(Point(win.getWidth()/2, 40), "相似得分为：").draw(win)
	
	Text(Point(win.getWidth()/2, 80), res).draw(win)
	
	Text(Point(win.getWidth()/2, 120), "图1和图2是同一个人.").draw(win)
	win.getMouse()
	win.close()

        
else:
	#print ("图1和图2不是同一个人.\n")
	win = GraphWin('检测结果', 300, 300)
	Text(Point(win.getWidth()/2, 40), "相似得分为：").draw(win)
	
	Text(Point(win.getWidth()/2, 80), res).draw(win)
	
	Text(Point(win.getWidth()/2, 120), "图1和图2不是同一个人.").draw(win)
	win.getMouse()
	win.close()
	

cv2.waitKey(100000)
