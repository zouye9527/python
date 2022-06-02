# -*- coding: UTF-8 -*-
import cv2
import time
import os
import sys

workpath=os.path.dirname(sys.argv[0])
os.chdir(workpath)          #指定py文件执行路径为当前工作路径

def getnowtime():
    mstime=int(1000*time.time())
    print(mstime)
    return mstime

capture = cv2.VideoCapture(0)
def main():
    
    while(1):
       ret, frame = capture.read()
       cv2.imshow('get', frame)
       savename=str(getnowtime())+'.jpg'
       cv2.imwrite(savename,frame)
       cv2.waitKey()

if __name__=="__main__":
    main()
