
# -*- coding: utf-8 -*-
# 
from aip import AipFace
import cv2
import base64
import sys
#from tkinter import *
from graphics import*
import tkinter as tk
from tkinter import filedialog
from time import sleep

sys.setrecursionlimit(1000000)
 

APP_ID = '26266987'
API_KEY = 'NUGbOm39G80AFZWGWh8F8f1Z'
SECRET_KEY = 'KNzF6nDWpNslHHEIj8HxtUkElXaKAf1e'
 
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def face_add(filepath,unit,num,name):  
  with open(filepath,'rb') as fp:
    base64_data = base64.b64encode(fp.read())
  image = str(base64_data, 'utf-8')
  imageType="BASE64"
  groupid=unit
  userid=num
  options = {}
  options["user_info"] = name
  result=aipFace.addUser(image,imageType,groupid,userid,options)
  if result['error_code']==0:
    win = GraphWin('检测结果',300,300)
    Text(Point(win.getWidth()/2, 80), "增加人脸成功").draw(win)
    print("增加人脸成功")
    win.getMouse()
    win.close()
  else:
    win = GraphWin('人脸注册结果',300,300)
    Text(Point(win.getWidth()/2, 80), "增加人脸失败").draw(win)
    if (result['error_msg'] == "face is already exist"):
      Text(Point(win.getWidth()/2, 120), "原因是：").draw(win)
      Text(Point(win.getWidth()/2, 150), "库中已经存在该人脸").draw(win)    
    win.getMouse()
    win.close()    
  #print(result)
         

if __name__=='__main__':

  
  filepath = "D:\\0\\1.JPG"

  # face_add('照片的路径','用户组名称','用户编号'，'用户名称')
  win = GraphWin('人脸注册', 500, 90)
  win.setBackground("yellow")
  Text(Point(win.getWidth()/2, 40), "请在文件夹中选择要 注册 的人脸图片").draw(win)
  sleep(1)
  root = tk.Tk()
  root.withdraw()
  filepath = filedialog.askopenfilename()

  root = tk.Tk()
  tk.Label(root, text="注册序号(座位号):").grid(row=0)
  tk.Label(root, text="注册姓名:").grid(row=1)
  e1 = tk.Entry(root)
  e2 = tk.Entry(root)
  e1.grid(row=0, column=1, padx=10, pady=5)
  e2.grid(row=1, column=1, padx=10, pady=5)
 
  def show():

    face_add(filepath,'class00075',int(e1.get()),e2.get().encode("utf-8").decode("latin1"))
  
  tk.Button(root, text="确定", width=10, command=show).grid(row=3, column=1, padx=10, pady=5)  
  root.mainloop()
