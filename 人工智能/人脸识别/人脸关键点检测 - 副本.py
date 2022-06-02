# -*- coding: utf-8 -*-
# 
from aip import AipFace
import cv2
import base64
import math
import matplotlib.pyplot as plt
from graphics import*
#import tkinter as tk
from tkinter import filedialog
from time import sleep

APP_ID = '26266991'
API_KEY = 'gryidKiq3pRGh8cnLDSB8dEy'
SECRET_KEY = 'q2g7SuVAEDEInYk0XqPqODr0MAP3GcH7'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

filepath = "C:\\Users\\lenovo\\Desktop\\face\\752\\faces.jpg"
win = GraphWin('人脸关键点检测', 500, 90)
win.setBackground("yellow")
Text(Point(win.getWidth()/2, 40), "请在文件夹中选择1张人脸图片进行关键点检测").draw(win)
sleep(1)
filepath = filedialog.askopenfilename()

from PIL import Image
im = Image.open(filepath)

with open(filepath, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')
imageType = "BASE64"

options = {}
options["face_field"] = "age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype"
options["max_face_num"] = 10
options["face_type"] = "LIVE"
 
result = aipFace.detect(image, imageType, options)
img = cv2.imread(filepath)
 
face_num = result['result']['face_num']
face_list = result['result']['face_list']

xvalue = []
yvalue = []
xvaluef = []
yvaluef = []

plt.figure(figsize=(9,6.5))
for num in range(0,int(face_num)):
       
    location = result['result']['face_list'][num-1]['location']
    landmark72 = result['result']['face_list'][num-1]['landmark72']

    xvaluef1 = []
    yvaluef1 = []
    xvaluef2 = []
    yvaluef2 = []
    xvaluef3 = []
    yvaluef3 = []
    xvaluef4 = []
    yvaluef4 = []
    xvaluef5 = []
    yvaluef5 = []
    xvaluef6 = []
    yvaluef6 = []
    xvaluef7 = []
    yvaluef7 = []
    xvaluef8 = []
    yvaluef8 = []

    for i in range(0,72):
        xvalue.append(landmark72[i]['x'])
        yvalue.append(landmark72[i]['y'])
        xvaluef.append(im.size[0]-landmark72[i]['x'])
        yvaluef.append(im.size[1]-landmark72[i]['y'])


    for i in range(0,13):
        xvaluef1.append(landmark72[i]['x'])
        yvaluef1.append(im.size[1]-landmark72[i]['y'])
 
    for i in range(13,21):
        xvaluef2.append(landmark72[i]['x'])
        yvaluef2.append(im.size[1]-landmark72[i]['y'])
    xvaluef2.append(landmark72[13]['x'])
    yvaluef2.append(im.size[1]-landmark72[13]['y'])

    for i in range(22,30):
        xvaluef3.append(landmark72[i]['x'])
        yvaluef3.append(im.size[1]-landmark72[i]['y'])
    xvaluef3.append(landmark72[22]['x'])
    yvaluef3.append(im.size[1]-landmark72[22]['y'])

    for i in range(30,38):
        xvaluef4.append(landmark72[i]['x'])
        yvaluef4.append(im.size[1]-landmark72[i]['y'])
    xvaluef4.append(landmark72[30]['x'])
    yvaluef4.append(im.size[1]-landmark72[30]['y'])

    for i in range(39,47):
        xvaluef5.append(landmark72[i]['x'])
        yvaluef5.append(im.size[1]-landmark72[i]['y'])
    xvaluef5.append(landmark72[39]['x'])
    yvaluef5.append(im.size[1]-landmark72[39]['y'])

    for i in range(47,57):
        xvaluef6.append(landmark72[i]['x'])
        yvaluef6.append(im.size[1]-landmark72[i]['y'])
    xvaluef6.append(landmark72[47]['x'])
    yvaluef6.append(im.size[1]-landmark72[47]['y'])

    for i in range(58,66):
        xvaluef7.append(landmark72[i]['x'])
        yvaluef7.append(im.size[1]-landmark72[i]['y'])
    xvaluef7.append(landmark72[58]['x'])
    yvaluef7.append(im.size[1]-landmark72[58]['y'])

    for i in range(66,71):
        xvaluef8.append(landmark72[i]['x'])
        yvaluef8.append(im.size[1]-landmark72[i]['y'])    
    xvaluef8.append(landmark72[66]['x'])
    yvaluef8.append(im.size[1]-landmark72[66]['y'])

    plt.subplot(2,2,num+2)
    plt.plot(xvaluef1,yvaluef1)#'ro',markersize=1
    plt.plot(xvaluef2,yvaluef2)
    plt.plot(xvaluef3,yvaluef3)
    plt.plot(xvaluef4,yvaluef4)
    plt.plot(xvaluef5,yvaluef5)
    plt.plot(xvaluef6,yvaluef6)
    plt.plot(xvaluef7,yvaluef7)
    plt.plot(xvaluef8,yvaluef8)
    plt.axis('off')

    Theta = location['rotation'] / 60 
    A = (int(location['left']),int(location['top']))
    B = (int(location['left'])+int(location['width']*math.cos(Theta)),int(location['top'])+int(location['width']*math.sin(Theta)))
    AC_Len = math.sqrt(location['width']**2 + location['height']**2)
    AC_Theta = math.atan(location['height']/location['width'])+location['rotation']/60 
    C = (int(location['left']) + int(AC_Len*math.cos(AC_Theta)), int(location['top'])+int(AC_Len*math.sin(AC_Theta)))
    D = (int(location['left'])-int(location['height']*math.sin(Theta)), int(location['top']) + int(location['height']*math.cos(Theta)))
    cv2.line(img, A, B, (0, 0, 255), 2)
    cv2.line(img, B, C, (0, 0, 255), 2)
    cv2.line(img, C, D, (0, 0, 255), 2)
    cv2.line(img, D, A, (0, 0, 255), 2)
 
plt.axis('off')
plt.subplot(2,2,1)
img = img[:,:,[2,1,0]]
plt.imshow(img,cmap='gray')
plt.plot(xvalue,yvalue,'bo',markersize=1)
plt.axis('off')
plt.show()

plt.figure(figsize=(9,6.5))
plt.imshow(img,'gray')
plt.plot(xvalue,yvalue,'bo',markersize=1)
plt.axis('off')
plt.show()


