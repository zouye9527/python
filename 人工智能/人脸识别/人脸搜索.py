# -*- coding: utf-8 -*-

from aip import AipFace
import cv2
import base64
import sys
from graphics import*
import tkinter as tk
from tkinter import filedialog
from time import sleep

from numpy import size
sys.setrecursionlimit(1000000) 
 

APP_ID = '26266987'
API_KEY = 'NUGbOm39G80AFZWGWh8F8f1Z'
SECRET_KEY = 'KNzF6nDWpNslHHEIj8HxtUkElXaKAf1e'
 
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_search(filepath):  
    with open(filepath, 'rb') as fp:
        base64_data = base64.b64encode(fp.read())
    image = str(base64_data, 'utf-8')
    imageType="BASE64"
    groupIdList='class00075'
    result=aipFace.search(image,imageType,groupIdList)
    img = cv2.imread(filepath)
    cv2.imshow('img', img)
    if (result['result']['user_list'][0]['score']>=70):
        win = GraphWin('人脸搜索结果',300,300)
        Text(Point(win.getWidth()/2, 40), "搜索结果：").draw(win)
        Text(Point(win.getWidth()/2, 65), result['result']['user_list'][0]['user_info']).draw(win)
        Text(Point(win.getWidth()/2, 120), "相似得分为：").draw(win)
        Text(Point(win.getWidth()/2, 145), result['result']['user_list'][0]['score']).draw(win)
        win.getMouse()
        win.close()
    else:
        win = GraphWin('人脸搜索结果',300,300)
        Text(Point(win.getWidth()/2, 40), "查找无结果……").draw(win)
        Text(Point(win.getWidth()/2, 120), "建议您先在人脸库中注册").draw(win)       
        win.getMouse()
        win.close()

if __name__=='__main__':
    
    filepath = "D:\\0\\1.JPG"
    win = GraphWin('人脸搜索', 500, 90)
    win.setBackground("yellow")
    Text(Point(win.getWidth()/2, 40), "请在文件夹中选择要搜索的人脸图片").draw(win)
    sleep(1)
    filepath = filedialog.askopenfilename()
    face_search(filepath)

  
