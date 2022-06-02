from aip import AipFace
import base64
import cv2
import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog 
 
APP_ID = '23935531'
API_KEY = 'auqVKL7FH8MYbN1RLyqCIo0t'
SECRET_KEY = 'n2LWuIOG7v3Djk8oR7kYzlArkBt58gqg'
 
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
 

filepath = "D:\\0\\1.JPG"
filepath = filedialog.askopenfilename()

with open(filepath, 'rb') as fp:
    content = base64.b64encode(fp.read())
image = str(content, 'utf-8')
 
imageType = "BASE64"
 
options = {}
options["face_field"] = "age"
options["max_face_num"] = 1
options["face_type"] = "LIVE"
 
result = aipFace.detect(image, imageType, options)
print(result)
 
 
img = cv2.imread(filepath)
face_num = result['result']['face_num']
 
for num in range(0, int(face_num)):
    print(num)
    location = result['result']['face_list'][num - 1]['location']
 
    Theta = location['rotation'] / 60  
    A = (int(location['left']), int(location['top']))
    B = (int(location['left']) + int(location['width'] * math.cos(Theta)),
         int(location['top']) + int(location['width'] * math.sin(Theta)))
    AC_Len = math.sqrt(location['width'] ** 2 + location['height'] ** 2)
    AC_Theta = math.atan(location['height'] / location['width']) + location['rotation'] / 60  
    C = (int(location['left']) + int(AC_Len * math.cos(AC_Theta)), int(location['top']) + int(AC_Len * math.sin(AC_Theta)))
    D = (int(location['left']) - int(location['height'] * math.sin(Theta)),
         int(location['top']) + int(location['height'] * math.cos(Theta)))
    cv2.line(img, A, B, (0, 0, 255), 2)
    cv2.line(img, B, C, (0, 0, 255), 2)
    cv2.line(img, C, D, (0, 0, 255), 2)
    cv2.line(img, D, A, (0, 0, 255), 2)
 
 
cv2.imshow('img', img)
cv2.waitKey(0)
 
plt.imshow(img, 'gray')
plt.show()
 